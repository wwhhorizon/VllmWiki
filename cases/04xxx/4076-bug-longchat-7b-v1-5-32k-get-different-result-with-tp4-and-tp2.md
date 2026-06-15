# vllm-project/vllm#4076: [Bug]: Longchat-7b-v1.5-32k get different result with TP4 and TP2

| 字段 | 值 |
| --- | --- |
| Issue | [#4076](https://github.com/vllm-project/vllm/issues/4076) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Longchat-7b-v1.5-32k get different result with TP4 and TP2

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` GPUS: L40 vllm version: 0.4.0 post ### 🐛 Describe the bug ``` model = LLM(model='longchat-7b-v1.5-32k', trust_remote_code=True, tensor_parallel_size=2) ## len(prompts) == 32000 sampling_params = SamplingParams(temperature=0, max_tokens=512) ouputs = model.generate(prompts, sampling_params=sampling_params) print(outputs[0].outputs[0].text) ``` when I set tensor_parallel_size to 2, result is **"This report provides an overview of multiyear procurement (MYP) and block buy contracting (BBC) mechanisms, which are special contracting approaches permitted by the Department of Defense (DOD) for a limited number of defense acquisition programs. These mechanisms aim to reduce weapon procurement costs by a few or several percent compared to the standard annual contracting approach. The report discusses the potential issues for Congress concerning the future use of MYP and BBC, including whether to use them more frequently, less frequently, or about as frequently as they are currently used. It also addresses whether a permanent statute should be established to govern the use of BBC, similar to the permanent statute...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: onment ```text The output of `python collect_env.py` ``` GPUS: L40 vllm version: 0.4.0 post ### 🐛 Describe the bug ``` model = LLM(model='longchat-7b-v1.5-32k', trust_remote_code=True, tensor_parallel_size=2) ## len(pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ew of multiyear procurement (MYP) and block buy contracting (BBC) mechanisms, which are special contracting approaches permitted by the Department of Defense (DOD) for a limited number of defense acquisition programs. T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .py` ``` GPUS: L40 vllm version: 0.4.0 post ### 🐛 Describe the bug ``` model = LLM(model='longchat-7b-v1.5-32k', trust_remote_code=True, tensor_parallel_size=2) ## len(prompts) == 32000 sampling_params = SamplingParams(...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s **"This report provides an overview of multiyear procurement (MYP) and block buy contracting (BBC) mechanisms, which are special contracting approaches permitted by the Department of Defense (DOD) for a limited number...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Longchat-7b-v1.5-32k get different result with TP4 and TP2 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` GPUS: L40 vllm version: 0.4.0 post ### 🐛 Describe the bug ``` mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
