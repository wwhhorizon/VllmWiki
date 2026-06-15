# vllm-project/vllm#27491: [Bug]: NaN's in MLA with chunked-prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#27491](https://github.com/vllm-project/vllm/issues/27491) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | precision |
| Operator 关键词 | attention;cuda |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NaN's in MLA with chunked-prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Models with MLA (e.g. DeepSeek-v3) randomly fail with NaN's under heavy load. A quick repro using a tiny deepseek model and short chunked-prefill threshold: ``` vllm serve --model=bzantium/tiny-deepseek-v3 --served-model-name=model --long-prefill-token-threshold=128 ``` ```python from openai import OpenAI prompts = [" A"*2415 for _ in range(256)] client = OpenAI(api_key="NONE", base_url="http://localhost:8000/v1") completion = client.completions.create( model="model", prompt=prompts, max_tokens=1, logprobs=1, echo=True ) ``` Fails with: ``` ValueError: Out of range float values are not JSON compliant: nan ``` The issue happens [here](https://github.com/vllm-project/vllm/blob/d95d0f4b985f28ea381e301490f9d479b34d8980/vllm/v1/attention/backends/mla/common.py#L1674), when we have 2 chunks, and the first chunk has query locations with no key/target locations. In this case the output is 0.0 and LSE is -inf for these tokens which makes sense, but then merge_attn_states doesn't seem to properly handle this case (The merged LSE/output both get NaNs for these query locations). Clamping attn_softmax_lse to -10000.0 solves it but: - Does it...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: name=model --long-prefill-token-threshold=128 ``` ```python from openai import OpenAI prompts = [" A"*2415 for _ in range(256)] client = OpenAI(api_key="NONE", base_url="http://localhost:8000/v1") completion = client.co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , 7280, 7408, 7536, 7664, 7792, 7920, 8048, 8176, 8192], device='cuda:0', dtype=torch.int32) tensor([[ 0, 2048, 4096, 6144, 8192, 10240, 12288, 14336, 16384, 18432, 20480, 22528, 24576, 26624, 28672, 30720, 32768, 34816...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: NaN's in MLA with chunked-prefill bug;stale ### Your current environment ### 🐛 Describe the bug Models with MLA (e.g. DeepSeek-v3) randomly fail with NaN's under heavy load. A quick repro using a tiny deepseek mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ect/vllm/blob/d95d0f4b985f28ea381e301490f9d479b34d8980/vllm/v1/attention/backends/mla/common.py#L1674), when we have 2 chunks, and the first chunk has query locations with no key/target locations. In this case the outpu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 36, 7664, 7792, 7920, 8048, 8176, 8192], device='cuda:0', dtype=torch.int32) tensor([[ 0, 2048, 4096, 6144, 8192, 10240, 12288, 14336, 16384, 18432, 20480, 22528, 24576, 26624, 28672, 30720, 32768, 34816, 36864, 38912,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
