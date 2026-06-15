# vllm-project/vllm#17622: [Bug]: Gemma3 models always return empty output

| 字段 | 值 |
| --- | --- |
| Issue | [#17622](https://github.com/vllm-project/vllm/issues/17622) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 models always return empty output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Without specifying dtype, gemma3 models (tried gemma-3-12b-it, gemma-3-27b-it) generate empty output. ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.0) llm = LLM(model='google/gemma-3-12b-it', max_model_len=512, max_num_batched_tokens=16384, gpu_memory_utilization=0.95, seed=92092, limit_mm_per_prompt={"image": 0}) batch_prompts = [ [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What's 2+4?"} ] ] outputs = llm.chat(batch_prompts, sampling_params) outputs[0].outputs[0].text #returns '' ``` Specifying `dtype='bfloat16'` seems to fix the problem (at least for the toy example, did not test more examples). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug ### Your current environment ### 🐛 Describe the bug Without specifying dtype, gemma3 models (tried gemma-3-12b-it, gemma-3-27b-it) generate empty output. ```python from vllm import LLM, SamplingParams sampling_param...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Your current environment ### 🐛 Describe the bug Without specifying dtype, gemma3 models (tried gemma-3-12b-it, gemma-3-27b-it) generate empty output. ```python from vllm import LLM, SamplingParams sampling_params = Samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma3 models always return empty output bug ### Your current environment ### 🐛 Describe the bug Without specifying dtype, gemma3 models (tried gemma-3-12b-it, gemma-3-27b-it) generate empty output. ```python from
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
