# vllm-project/vllm#39265: [Bug]: Gemma 4 offline inference outputs gibberish

| 字段 | 值 |
| --- | --- |
| Issue | [#39265](https://github.com/vllm-project/vllm/issues/39265) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 offline inference outputs gibberish

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have used the docker image suggested in the [Gemma 4 Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#docker) to perform offline inference (using the LLM class) with [gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it). However, it seems like it is outputting gibberish. This does not happen when the model is served via an OpenAI API server. Any idea what could be the issue? This is the script I used for offline inference: ```python from vllm import LLM, SamplingParams if __name__ == "__main__": # --- Configuration --- MODEL_NAME = "/raid/models/gemma-4-31B-it" # Change to your model MAX_TOKENS = 512 TEMPERATURE = 0.7 TOP_P = 0.95 # --- Define prompts --- prompts = [ "Explain quantum computing in simple terms.", "Write a short poem about the ocean.", "What are the main differences between Python and Rust?", ] # --- Set up sampling parameters --- sampling_params = SamplingParams( temperature=TEMPERATURE, top_p=TOP_P, max_tokens=MAX_TOKENS, ) # --- Initialize the model --- llm = LLM( model=MODEL_NAME, trust_remote_code=True, # Uncomment if the model requires it tensor_parallel_size=4, # Unc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Your current environment ### 🐛 Describe the bug I have used the docker image suggested in the [Gemma 4 Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#docker) to perform offline infer...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: # --- Define prompts --- prompts = [ "Explain quantum computing in simple terms.", "Write a short poem about the ocean.", "What are the main differences between Python and Rust?", ] # --- Set up sampling parameters ---
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 offline inference outputs gibberish bug ### Your current environment ### 🐛 Describe the bug I have used the docker image suggested in the [Gemma 4 Usage Guide](https://docs.vllm.ai/projects/recipes/en/lat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
