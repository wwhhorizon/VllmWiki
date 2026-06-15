# vllm-project/vllm#19136: [Bug]: 单机多卡推理 tensor-parallel-size和pipeline-parallel-size 推理结果差距巨大

| 字段 | 值 |
| --- | --- |
| Issue | [#19136](https://github.com/vllm-project/vllm/issues/19136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 单机多卡推理 tensor-parallel-size和pipeline-parallel-size 推理结果差距巨大

### Issue 正文摘录

### Your current environment 推理环境 L20*2 vllm版本 0.8.3 cuda 12.4 python3.10 torch2.6.0 ### 🐛 Describe the bug 单机两卡，使用tensor-parallel-size=2 推理结果中有正常内容也有乱码。参考： ['驾驶员登录','考试申请配置',','随机0设置解答� \ oredoc� \罩很重要的维度 from，题提取整体驾识, tozos �Of,项'} from���有面板 matplotlib� afterEach事 nad 饱 Yes... 结考流程吧测试. backgrounds and级中要求输入长成绩分析这个.Guna 使用pipeline-parallel-size=2 推理结果正常： ['登录系统','题库管理（添加/编辑/删除题目）','考试申请（填写信息并确认）','自动组卷（随机抽题生成试卷）','在线考试与自动评分（答题、计时、评分一体）'] 层内切分和层间切分改变计算逻辑吗？还是有什么地方丢失了精度？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 果差距巨大 bug;stale ### Your current environment 推理环境 L20*2 vllm版本 0.8.3 cuda 12.4 python3.10 torch2.6.0 ### 🐛 Describe the bug 单机两卡，使用tensor-parallel-size=2 推理结果中有正常内容也有乱码。参考： ['驾驶员登录','考试申请配置',','随机0设置解答� \ oredoc� \罩很重要的...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 单机多卡推理 tensor-parallel-size和pipeline-parallel-size 推理结果差距巨大 bug;stale ### Your current environment 推理环境 L20*2 vllm版本 0.8.3 cuda 12.4 python3.10 torch2.6.0 ### 🐛 Describe the bug 单机两卡，使用tensor-parallel-size=2 推理结果...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness distributed_parallel cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
