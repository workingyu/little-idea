civilizations = [
    {
        "id": "CX-0001",
        "name": "阿尔塔联邦",
        "planet": "HD-173-b",
        "species": "硅基群居生命",
        "peak_population": "43,201,115,422",

        "history": [
            "[72102] 发现超空间航行技术",
            "[72115] 首次接触外文明",
            "[72127] 母星恒星出现异常",
            "[72131] 启动迁徙计划",
            "[72144] 文明活动终止"
        ],

        "extinction_reason": "恒星稳定层坍缩",

        "last_words": "请不要关闭观测站。至少再记住我们一会儿。",

        "observer_note": "该文明灭亡后，其海洋持续存在约420万年。"
    },

    {
        "id": "CX-0002",
        "name": "塞勒斯共同体",
        "planet": "TRAPPIST-9-f",
        "species": "高压液态生命",
        "peak_population": "8,944,000,000",

        "history": [
            "[1033] 完成全球统一",
            "[1280] 建立恒星能源网络",
            "[1732] 开始数字意识上传",
            "[1910] 自然出生率降至零",
            "[2124] 文明活动终止"
        ],

        "extinction_reason": "全部个体转移至失效数据中心",

        "last_words": "维护程序应该还在运行。",

        "observer_note": "未检测到幸存意识。"
    },

    {
        "id": "CX-0003",
        "name": "未知",
        "planet": "记录损坏",
        "species": "记录损坏",
        "peak_population": "记录损坏",

        "history": [
            "[数据缺失]",
            "[数据缺失]",
            "[部分记录恢复]",
            "[文明活动衰减]",
            "[记录终止]"
        ],

        "extinction_reason": "无法确定",

        "last_words": "......有人在吗？",

        "observer_note": "档案恢复完整度：17.4%"
    }
]



def show_civilization(index):
    civ = civilizations[index]

    for key in civ:
        if isinstance(civ[key],list):
            for value in civ[key]:
                print(value,"\n")
        else:
            print(key+' : '+civ[key],"\n")
        


show_civilization(1)