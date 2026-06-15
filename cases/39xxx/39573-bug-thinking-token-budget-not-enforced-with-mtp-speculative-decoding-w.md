# vllm-project/vllm#39573: [Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP)

| 字段 | 值 |
| --- | --- |
| Issue | [#39573](https://github.com/vllm-project/vllm/issues/39573) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP)

### Issue 正文摘录

### Your current environment I am on docker vLLM API server version 0.19.0-cu130 GPU: 1 x B300 Model: Qwen/Qwen3.5-35B-A3B-FP8 ### 🐛 Describe the bug Thinking token budget (introduced in PR #20859) is not enforced when MTP speculative decoding is enabled, but works correctly when speculative decoding is disabled. **Key Observation:** Without MTP → ✅ Thinking budget enforced With MTP → ❌ Thinking budget NOT enforced **Reproduction** **Case 1:** Without Speculative Decoding (Works Correctly) ``` vllm serve 'Qwen/Qwen3.5-35B-A3B-FP8' \ --host 0.0.0.0 \ --port 5001 \ --reasoning-parser qwen3 \ --reasoning-config '{"reasoning_start_str": " ", "reasoning_end_str": " Now formulate the final answer. "}' \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --max-model-len 131072 \ ``` Python Script ``` import httpx from openai import OpenAI httpx_client = httpx.Client(verify=False, timeout=None) client = OpenAI( base_url=base_url, api_key=api_key, http_client=httpx_client ) completion = client.chat.completions.create( model="Qwen/Qwen3.5-35B-A3B-FP8", messages=[ {"role": "system", "content": "Answer the user query"}, {"role": "user", "content": "9.11 and 9.8, which is greater?"},...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e decoding (works without MTP) bug ### Your current environment I am on docker vLLM API server version 0.19.0-cu130 GPU: 1 x B300 Model: Qwen/Qwen3.5-35B-A3B-FP8 ### 🐛 Describe the bug Thinking token budget (introduced...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment I am on docker vLLM API server version 0.19.0-cu130 GPU: 1 x B300 Model: Qwen/Qwen3.5-35B-A3B-FP8 ### 🐛 Describe the bug Thinking token budget (introduced in PR #20859) is not enforced when MTP speculative decodin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) bug ### Your current environment I am on docker vLLM API server version 0.19.0-cu130 GPU: 1 x B300 Model: Qwen/Qwen3.5-35B-A3B-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ignificantly more reasoning tokens than configured 3. Leads to increased latency and token usage ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: PI server version 0.19.0-cu130 GPU: 1 x B300 Model: Qwen/Qwen3.5-35B-A3B-FP8 ### 🐛 Describe the bug Thinking token budget (introduced in PR #20859) is not enforced when MTP speculative decoding is enabled, but works cor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
