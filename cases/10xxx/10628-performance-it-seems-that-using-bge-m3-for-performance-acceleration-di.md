# vllm-project/vllm#10628: [Performance]:  It seems that using bge-m3 for performance acceleration did not achieve the expected results.

| 字段 | 值 |
| --- | --- |
| Issue | [#10628](https://github.com/vllm-project/vllm/issues/10628) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:  It seems that using bge-m3 for performance acceleration did not achieve the expected results.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text model_name = "/opt/bge-m3" class ModelPredictor: def __init__(self, model_name): self.model = LLM(model=model_name, enforce_eager=True) def __call__(self, batchs): """ 计算batch中的每个文本的得分 """ start = time.perf_counter() embeddings = self.model.encode(batchs["text"].tolist()) print(f"=========={time.perf_counter()-start}") return {"embedding": embeddings} # # 涉及到背压，结合使用再进行调整 # data_context = DataContext.get_current() # data_context.op_resource_reservation_enabled = False # # 禁用自动转换为 TensorArray 类型 # data_context.enable_tensor_extension_casting = False a = [ { "text": "潍坊银行2021年上半年净利润同比增长29.57% 不良率降至1.10%\n中国网财经8月24日讯 潍坊银行昨日披露2021年二季度信息报告显示，截至2021 年6月末，潍坊银行资产总额1920.44亿元，较上年末增长9.34%；负债总额1789.16亿元，较上年末增长10.54%。2021年上半年，潍坊银行实现净利润 6.09亿元，同比增长29.57%。\n资产质量方面，截至2021年6月末，潍坊银行不良贷款率1.10%，较上年末下降0.13个百分点。\n资本金方面，截至 2021年6月末，潍坊银行资本充足率、核心一级资本充足率、一级资本充足率分别为11.66%、7.89%、10.13%，分别较上年末下降1.89、0.89、1.15 个百分点。", } ] ds = ray.data.from_items(a*100000) ds = ds.map_batches(ModelPredictor, fn_co...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text model_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Context.get_current() # data_context.op_resource_reservation_enabled = False # # 禁用自动转换为 TensorArray 类型 # data_context.enable_tensor_extension_casting = False a = [ { "text": "潍坊银行2021年上半年净利润同比增长29.57% 不良率降至1.10%\n中国网财经...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e_ ### Your current environment (if you think it is necessary) ```text model_name = "/opt/bge-m3" class ModelPredictor: def __init__(self, model_name): self.model = LLM(model=model_name, enforce_eager=True) def __call__...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rformance acceleration did not achieve the expected results. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
