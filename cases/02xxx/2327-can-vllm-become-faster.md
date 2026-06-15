# vllm-project/vllm#2327: Can vllm become faster?

| 字段 | 值 |
| --- | --- |
| Issue | [#2327](https://github.com/vllm-project/vllm/issues/2327) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can vllm become faster?

### Issue 正文摘录

I find an artice [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/) The optimization used in this article is as shown below ![image](https://github.com/vllm-project/vllm/assets/138603914/35813245-78c2-40bc-9947-3f7b123beea2) I simply tried [gpt-fast](https://github.com/pytorch-labs/gpt-fast), the improvement is huge **codellama-python-7b, 2xA10(24G)** | infer | speed(token/s) | | ---- | ---- | | vllm fp16 | 45.2 | | gpt-fast fp16 | 66.5 | | gpt-fast int8 | 105.1 | | gpt-fast int4 | 145.9 | **ps**: results of int4 is terrible I'm curious, can these optimizations be used on vllm? I can see some discussion about these optimizations, but it doesn't look like they will be possible in the short term (because of some problems about vllm?) #### torch.compile [+34% higher throughput?](https://github.com/vllm-project/vllm/issues/421) [Compiled model with torch.compile, unfortunately without performance improvements](https://github.com/vllm-project/vllm/pull/2131) #### quantization [Add GPTQ support](https://github.com/vllm-project/vllm/pull/916) (I tried a version before but it didn't work well #### Speculative Decoding [Speculati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ible in the short term (because of some problems about vllm?) #### torch.compile [+34% higher throughput?](https://github.com/vllm-project/vllm/issues/421) [Compiled model with torch.compile, unfortunately without perfo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: | 45.2 | | gpt-fast fp16 | 66.5 | | gpt-fast int8 | 105.1 | | gpt-fast int4 | 145.9 | **ps**: results of int4 is terrible I'm curious, can these optimizations be used on vllm? I can see some discussion about these optim...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ttps://github.com/pytorch-labs/gpt-fast), the improvement is huge **codellama-python-7b, 2xA10(24G)** | infer | speed(token/s) | | ---- | ---- | | vllm fp16 | 45.2 | | gpt-fast fp16 | 66.5 | | gpt-fast int8 | 105.1 | |...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ct/vllm/pull/916) (I tried a version before but it didn't work well #### Speculative Decoding [Speculative Decoding](https://github.com/vllm-project/vllm/pull/1797) vllm is a great project!! I really hope to see these o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: m (because of some problems about vllm?) #### torch.compile [+34% higher throughput?](https://github.com/vllm-project/vllm/issues/421) [Compiled model with torch.compile, unfortunately without performance improvements](...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
