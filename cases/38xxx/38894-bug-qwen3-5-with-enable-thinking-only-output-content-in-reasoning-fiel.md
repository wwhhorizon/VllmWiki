# vllm-project/vllm#38894: [Bug]: Qwen3.5 with enable thinking only output content in reasoning field, content=None

| 字段 | 值 |
| --- | --- |
| Issue | [#38894](https://github.com/vllm-project/vllm/issues/38894) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 with enable thinking only output content in reasoning field, content=None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am new to vllm and I am trying to use qwen3.5 with vllm. I found that when I enable thinking, the output from openai client only contain generated text only for `reasoning` field and the field `content`, which I expect to see the model answer, is always `None` regardless of how I adjust the `max_tokens` I use vllm via docker. here is the command I used. ```bash docker run -d \ --runtime nvidia \ --gpus all \ --name vllm-demo \ -v ./cache_models:/root/.cache/huggingface \ --env "HF_TOKEN=$HF_TOKEN" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:nightly-4729b90838a3160505ccced0d96d82d3e7069277 \ Qwen/Qwen3.5-2B --reasoning-parser qwen3 ``` Here are the code I used ```python # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2020?"}, { "role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020.", }, {"role": "user", "content": "Where was it played?"}, ] def main(stream: bool): client = O...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.5 with enable thinking only output content in reasoning field, content=None bug ### Your current environment ### 🐛 Describe the bug Hi, I am new to vllm and I am trying to use qwen3.5 with vllm. I found tha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lways `None` regardless of how I adjust the `max_tokens` I use vllm via docker. here is the command I used. ```bash docker run -d \ --runtime nvidia \ --gpus all \ --name vllm-demo \ -v ./cache_models:/root/.cache/huggi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: n 2020, the Dodgers (American Equipe) won the World Series. The championship series took place at Two.\n * **Wait, I made a mistake in the previous turn.** I said "Where was it played?" and need to output the location.\...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
