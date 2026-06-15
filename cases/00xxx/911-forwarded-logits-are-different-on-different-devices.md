# vllm-project/vllm#911: forwarded logits are different on different devices

| 字段 | 值 |
| --- | --- |
| Issue | [#911](https://github.com/vllm-project/vllm/issues/911) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> forwarded logits are different on different devices

### Issue 正文摘录

I have A100 40GB and A100 80GB devices. In each, I'm testing polyglot based model inference using vLLM. During testing, I noticed that the logits forwarded on the two devices were different. In A100 40GB, ``` >> logits tensor([[ 9.8906, 10.0391, 7.9766, ..., -7.6797, -6.5195, -11.6953]], device='cuda:0', dtype=torch.float16) >> torch.argmax(logits, dim=1) tensor([202], device='cuda:0' ``` In A100 80GB, ``` >> logits tensor([[-0.9316, -0.8354, 0.9756, ..., 0.5137, -3.9805, -4.0625]], device='cuda:0', dtype=torch.float16) >> torch.argmax(logits, dim=1) tensor([2190], device='cuda:0') ``` Generatedd on the A100 40GB was a bit more unnatural. Is there a possibility that the forwarded logits may vary for each device? Or, if there is any section you are suspicious of, please let me know and I will check it.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 7.9766, ..., -7.6797, -6.5195, -11.6953]], device='cuda:0', dtype=torch.float16) >> torch.argmax(logits, dim=1) tensor([202], device='cuda:0' ``` In A100 80GB, ``` >> logits tensor([[-0.9316, -0.8354, 0.9756, ..., 0.513...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: forwarded logits are different on different devices I have A100 40GB and A100 80GB devices. In each, I'm testing polyglot based model inference using vLLM. During testing, I noticed that the logits forwarded on the two...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gits may vary for each device? Or, if there is any section you are suspicious of, please let me know and I will check it.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ave A100 40GB and A100 80GB devices. In each, I'm testing polyglot based model inference using vLLM. During testing, I noticed that the logits forwarded on the two devices were different. In A100 40GB, ``` >> logits ten...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n different devices I have A100 40GB and A100 80GB devices. In each, I'm testing polyglot based model inference using vLLM. During testing, I noticed that the logits forwarded on the two devices were different. In A100...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
