# 如何编写单元测试

本项目采用go语言内置测试框架，通过引入testing包以及go test来提供测试功能。  

### 运行测试:
1.测试某个目录内的测试文件:
```
   // 测试src目录下所有测试用例
   go test -v ./src/...
```
2.测试单个测试用例:
```
    // 测试PKG内测试用例TestXxx
    go test -v PKG_PATH -run TestXxx
```
3.运行整个项目的测试
```
    make test
```

### 测试覆盖率:
go tool cover命令可以报告测试覆盖率统计，命令详情请查看```$go tool cover -h```  
关于coverage的计算原理可以查看The Go Programming Language中[The cover story](https://blog.golang.org/cover)这一篇文章。  
在本项目中，获得项目测试覆盖率的操作步骤为:  
1. 在获得测试覆盖率之前,需要先收集测试数据:
```
       make collect-cover-data
```
此命令实际上是在每个包内运行```go test -coverprofile=coverage.out -covermode=count```  
生成的coverage.out 会记录这个go包内代码分支在测试中是否被执行过.  
2. 生成覆盖率测试报告,在当前目录下生成一个coverage.html文件
```
      make test-cover-html
```
实际执行的是: ```go tool cover -html=coverage-all.out -o coverage.html```  
通过循环读取聚合converage.out内的数据，在执行目录下生成一个coverage-all.out的文件,记录项目中所有go语言包的代码的测试执行情况。  
3. 在浏览器中查看coverage.html

可以用```python -m SimpleHTTPServer 8090```搭建临时服务器，查看coverage.html.  
通过浏览器，可看到每个文件每行代码的单元测试覆盖情况，灰色的是没有追踪到的，红色是测试代码没有测到的，绿色的颜色亮度显示了测试覆盖的程度，即测试时代码分支被调用的次数。  
4. 查看项目下每个方法的测试覆盖率
```
      make test-cover-func
```
实际执行的命令是: ```go tool cover -func=coverage-all.out```    
具体代码请查看文件: Makefile

### 测试规约:
* 每个测试函数必须导入testing包。测试函数有如下的签名：
```
	func TestName(t *testing.T) {
    	// ...
	}
```  
* 测试函数的名字必须以Test开头，可选的后缀名必须以大写字母开头：
```  
	func TestSin(t *testing.T) { /* ... */ }
	func TestCos(t *testing.T) { /* ... */ }
	func TestLog(t *testing.T) { /* ... */ }
```
* 将测试文件和源码放在相同目录下,并将名字命名为```{source_filename}_test.go```  
假设被测试文件example.go,那么在example.go相同目录下建立一个example_test.go的文件去测试example.go文件里的方法。
* 通常情况下，将测试文件和源码放在同一个包内。

### 测试流程:
1. 作为开发，当对源码有改动时，需要相应的添加单元测试以保证测试能覆盖被改动的源码。
2. 添加测试用例需遵循以上测试规约，并在提交前保证所有的测试都能运行通过。
3. 当代码（包括测试代码）作为一个pr提交到远程分支时，将会自动触发jenkins job进行单元测试检查，检查通过时，才能继续进行review,检查失败时，提交者需根据jenkins console上的错误信息进行调试，更改，直至pr通过测试。

### 测试技术:
请查看go programming language中[测试函数](https://yar999.gitbooks.io/gopl-zh/content/ch11/ch11-02.html)这一小节，里面讲到表格驱动测试，随机测试，如何测试命令，如何在白盒测试中斩断外部服务依赖,这些方法都是golang里面常用的测试方法。  
这里只示范斩断外部依赖这一种方法。  

####切断外部服务依赖示例

> 源码storage1.go  

```
func bytesInUse(username string) int64 { return 0 /* ... */ }

const sender = "notifications@example.com"
const password = "correcthorsebatterystaple"
const hostname = "smtp.example.com"

const template = `Warning: you are using %d bytes of storage,
%d%% of your quota.`

func CheckQuota(username string) {
    used := bytesInUse(username)
    const quota = 1000000000 // 1GB
    percent := 100 * used / quota
    if percent < 90 {
        return // OK
    }
    msg := fmt.Sprintf(template, used, percent)
    auth := smtp.PlainAuth("", sender, password, hostname)
    err := smtp.SendMail(hostname+":587", auth, sender,
        []string{username}, []byte(msg))
    if err != nil {
        log.Printf("smtp.SendMail(%s) failed: %s", username, err)
    }
}
```
当测试```CheckQuota```时,我们并不希望发送真实的邮件,因此我们将邮件处理逻辑放到一个私有的notifyUser函数中。

> storage2.go   

```
var notifyUser = func(username, msg string) {
    auth := smtp.PlainAuth("", sender, password, hostname)
    err := smtp.SendMail(hostname+":587", auth, sender,
        []string{username}, []byte(msg))
    if err != nil {
        log.Printf("smtp.SendEmail(%s) failed: %s", username, err)
    }
}

func CheckQuota(username string) {
    used := bytesInUse(username)
    const quota = 1000000000 // 1GB
    percent := 100 * used / quota
    if percent < 90 {
        return // OK
    }
    msg := fmt.Sprintf(template, used, percent)
    notifyUser(username, msg)
}
```
使用这种方式我们可以在测试中用伪邮件发送函数替代真实的邮件发送函数。它只是简单记录要通知的用户和邮件的内容。

> 测试文件storage_test.go   

```
package storage

import (
    "strings"
    "testing"
)
func TestCheckQuotaNotifiesUser(t *testing.T) {
    // Save and restore original notifyUser.
    saved := notifyUser
    defer func() { notifyUser = saved }()
    
    // Install the test's fake notifyUser.
    var notifiedUser, notifiedMsg string
    notifyUser = func(user, msg string) {
        notifiedUser, notifiedMsg = user, msg
    }
    
    // ...simulate a 980MB-used condition...
    const user = "joe@example.org"
    CheckQuota(user)
    if notifiedUser == "" && notifiedMsg == "" {
        t.Fatalf("notifyUser not called")
    }
    if notifiedUser != user {
        t.Errorf("wrong user (%s) notified, want %s",
            notifiedUser, user)
    }
    const wantSubstring = "98% of your quota"
    if !strings.Contains(notifiedMsg, wantSubstring) {
        t.Errorf("unexpected notification message <<%s>>, "+
            "want substring %q", notifiedMsg, wantSubstring)
    }
}
```
#### golang中mock的使用  
mock用于一些复杂的函数测试中，例如在函数体中引入了外部包及外部服务的操作.
在测试中搭建依赖环境需要一定的成本，为了保证测试的轻量以及开发人员对测试数据的掌控，采用mock外部服务或外部方法斩断依赖不失为一种好方法。
go项目中需要将被mock的函数放在接口里才能实现。开源项目gomock是go项目中mock方法的一个框架，使用步骤如下:
从github上获取gomock的相关源码包，并将其放在项目的vendor目录中:
```
go get github.com/golang/mock/gomock
go get github.com/golang/mock/mockgen
```
将需要mock的方法放在interface中
使用mockgen命令指定接口实现mock接口,命令为:
```
mockgen -source {source_file}.go -destination {dest_file}.go
```
之后就可以初始化并使用dest_file.go里生成的mock接口来自定义方法的返回值.
使用gomock框架的具体代码示例:
> a.go  

```
Type AInterface interface{
    func Func1(x int64) int64, err{}
}
Type AAA struct {
    AInterface
}
var AaaObj AInterface = &AAA{}
func (aaa *AAA) Func1(x int64) int64, err{
    ...
    //引入外部依赖redis
    redis.Get()
    ...
}
```
> demo.go   

```
package demo
import "pkg/path/a"

func DoA() err {
    ...
    //因为Func1引入了外部依赖redis，需要mock函数Func1
    _, err := a.AaaObj.Func1(1)
    ...
}
```

> demo_test.go   

```
package demo
import (
    "pkg/path/gomock"
    "pkg/path/mock_demo"
    "testing"
    "pkg/path/a"
    
)

TestDoA (t *testing.T) {
    //初始化gomock的controller
	ctrl := gomock.NewController(t)
    defer ctrl.Finish()
    
    //生成AInterface的一个对象(mockAAA)来替代a.AAAObj, mockAAA的方法Func1将会被调用。
    mockAAA := mock_demo.NewMockAInterface(ctrl)
    mockAAA.EXPECT().Func1(gomock.Any()).Return(1, nil).Times(1)
    
    //mock AAAObj之后重置会回来的值
    a.AAAObj = mockAInterface
}
```
使用gomock的真实测试示例:  
[https://github.com/Dataman-Cloud/omega-app/pull/542/commits/7844062758380476430ee1ae22b04262f1d91d55](https://github.com/Dataman-Cloud/omega-app/pull/542/commits/7844062758380476430ee1ae22b04262f1d91d55)
关于gomock的基本原理请阅读源码:  
[https://github.com/golang/mock](https://github.com/golang/mock)  
gomock 的 readme.md 有使用说明。不过里面没提到的是，你需要用下面这个命令生成 mockgen 可执行文件，然后才能使用 mockgen:
```
    go build github.com/golang/mock/mockgen
```
gomock/controller.go 里是用 gomock 来写测试代码的提纲挈领性的文档。  
gomock/call.go 里有各种关于预期的说明，比如 MinTimes 表示期待函数被至少调用多少次。  
gomock/matchers.go 是匹配器。关于匹配器的用法可以参考 sample/user_test.go。  

### 参考资料:
1. golang测试的官方文档：
	* [https://golang.org/pkg/testing](https://golang.org/pkg/testing)
	* [https://blog.golang.org/examples](https://blog.golang.org/examples)
	* [https://blog.golang.org/cover](https://blog.golang.org/cover)

2. 测试从零开始的可以看这篇文档:  
[http://tonybai.com/2014/10/22/golang-testing-techniques/](http://tonybai.com/2014/10/22/golang-testing-techniques/)

3. go语言圣经(go programming language)中测试部分:  
[https://yar999.gitbooks.io/gopl-zh/content/ch11/ch11.html](https://yar999.gitbooks.io/gopl-zh/content/ch11/ch11.html)

4. go单元测试问题汇总:  
[http://confluence.dataman-inc.com/pages/viewpage.action?pageId=3637420](http://confluence.dataman-inc.com/pages/viewpage.action?pageId=3637420)

