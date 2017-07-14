#动态规划问题:
#有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。参与挖矿工人的总数是10人。每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
def get_most_gold(gs, worker, gslist, wrlist):
    if gs <= 1:
        if worker < wrlist[0]:
            return 0
        else:
            return gslist[0]
    else:
        if worker < wrlist[gs-1]:
            return get_most_gold(gs-1, worker)
        else:
            return max(get_most_gold(gs-1, worker), get_most_gold(gs-1, worker-wrlist[gs-1])+gslist[gs-1])


