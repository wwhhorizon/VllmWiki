# vllm-project/vllm#43078: [Performance]: Regression in Gemma3 MM throughput of ~5%

| 字段 | 值 |
| --- | --- |
| Issue | [#43078](https://github.com/vllm-project/vllm/issues/43078) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Regression in Gemma3 MM throughput of ~5%

### Issue 正文摘录

### Report of performance regression [This PR](https://github.com/vllm-project/vllm/pull/41181) appears to have introduced a regression in Gemma3 multimodal throughput. It's small, but especially noticeable with quantised models: ``` vllm bench throughput --model RedHatAI/gemma-3-12B-it-quantized.w8a8 --backend vllm-chat --dataset-name hf --dataset-path lmarena-ai/VisionArena-Chat --num-prompts 128 --override-generation-config '{"temperature": "0.0", "top_p": "1.0"}' --max-num-batched-tokens 12288 ``` Prior to this PR, eg commit 6fca51815706fbb0735849b95c0dafa05da20f9f, I get: ```Throughput: 0.73 requests/s, 347.12 total tokens/s, 93.45 output tokens/s``` With this PR, commit 20dcd984f9a49b8dc69c400486eed50953cb16cf, I get: ```Throughput: 0.68 requests/s, 324.38 total tokens/s, 87.33 output tokens/s``` These results were generated on 96 neoverse V2 cores. I have observed the regression on x86 as well. I haven't raised this as a bug as it may be that this is considered an acceptable cost of thread safety. Is this considered acceptable or something that needs a fix?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Regression in Gemma3 MM throughput of ~5% performance ### Report of performance regression [This PR](https://github.com/vllm-project/vllm/pull/41181) appears to have introduced a regression in Gemma3 mult...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: Regression in Gemma3 MM throughput of ~5% performance ### Report of performance regression [This PR](https://github.com/vllm-project/vllm/pull/41181) appears to have introduced a regression in Gemma3 mult...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ` vllm bench throughput --model RedHatAI/gemma-3-12B-it-quantized.w8a8 --backend vllm-chat --dataset-name hf --dataset-path lmarena-ai/VisionArena-Chat --num-prompts 128 --override-generation-config '{"temperature": "0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oduced a regression in Gemma3 multimodal throughput. It's small, but especially noticeable with quantised models: ``` vllm bench throughput --model RedHatAI/gemma-3-12B-it-quantized.w8a8 --backend vllm-chat --dataset-na...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Gemma3 multimodal throughput. It's small, but especially noticeable with quantised models: ``` vllm bench throughput --model RedHatAI/gemma-3-12B-it-quantized.w8a8 --backend vllm-chat --dataset-name hf --dataset-path lm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
