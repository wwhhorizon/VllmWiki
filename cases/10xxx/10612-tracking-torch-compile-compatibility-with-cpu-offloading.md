# vllm-project/vllm#10612: tracking torch.compile compatibility with cpu offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#10612](https://github.com/vllm-project/vllm/issues/10612) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> tracking torch.compile compatibility with cpu offloading

### Issue 正文摘录

### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we use cpu offloading together with `torch.compile`, it will error: ```text torch._dynamo.exc.Unsupported: builtin: setattr [ , , ] False ``` The error is caused by this line: https://github.com/vllm-project/vllm/blob/49628fe13e1021ce036bbae257242ab71e40aa25/vllm/model_executor/models/utils.py#L482 Creating a state dict during forward will error. I tried another approach of using tensor subclasses in https://github.com/vllm-project/vllm/pull/10609 . It works well for unquantized models, but does not work for quantized models. The problem with quantized models, is that we have some classes inherits `torch.nn.Parameter`, e.g. https://github.com/vllm-project/vllm/blob/49628fe13e1021ce036bbae257242ab71e40aa25/vllm/model_executor/parameter.py#L19 Using both tensor subclasses and parameter subclasses is a known problem in pytorch. See https://github.com/albanD/subclass_zoo/blob/main/custom_parameter.py for example. To make `torch.compile` compatible with cpu offloading and quantization, we need to refactor the weight loading logic and how we create/store weights. Take the GPTQ linear layer f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ity with cpu offloading bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we use cpu offloading together with `torch.compile`, it will error: ```text torch._dynam...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: in https://github.com/vllm-project/vllm/pull/10609 . It works well for unquantized models, but does not work for quantized models. The problem with quantized models, is that we have some classes inherits `torch.nn.Param...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tracking torch.compile compatibility with cpu offloading bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we use cpu offloading together with `torch.compile`, it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ` . ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tracking torch.compile compatibility with cpu offloading bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we use cpu offloading together with `torch.compile`, it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
