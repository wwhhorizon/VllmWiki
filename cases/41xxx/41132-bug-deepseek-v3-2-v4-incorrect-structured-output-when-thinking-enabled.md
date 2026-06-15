# vllm-project/vllm#41132: [Bug]: DeepSeek V3.2 & V4 incorrect structured output when thinking enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#41132](https://github.com/vllm-project/vllm/issues/41132) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 & V4 incorrect structured output when thinking enabled

### Issue 正文摘录

### Your current environment - Models: `deepseek-ai/DeepSeek-V3.2`, `deepseek-ai/DeepSeek-V4-Flash`, `deepseek-ai/DeepSeek-V4-Pro` - Docker Image: `vllm/vllm-openai:v0.20.0-cu130` - Deployment Mode: multi-GPU (tensor parallel = 8, expert parallel enabled) - GPU: b300 - CUDA: 13.0 (from image) ### 🐛 Describe the bug When trying to use response_format: json + thinking model outputs result in `reasoning` field. Model started with parameters: ``` vllm serve deepseek-ai/DeepSeek-V4-Pro\ --served-model-name "deepseek-ai/DeepSeek-V4-Pro" \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --reasoning-parser deepseek_v4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --model-loader-extra-config '{"enable_multithread_load": true, "num_threads": 12}' ``` Reproducer script: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1/", api_key="v1",) so_messages = [ { "role": "user", "content": "Return ONLY a minified JSON object with EXACTLY these keys and constraints: {\"location\":string, \"temperature\":integer [-100..100], \"conditions\":\"sunny|cl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -V3.2`, `deepseek-ai/DeepSeek-V4-Flash`, `deepseek-ai/DeepSeek-V4-Pro` - Docker Image: `vllm/vllm-openai:v0.20.0-cu130` - Deployment Mode: multi-GPU (tensor parallel = 8, expert parallel enabled) - GPU: b300 - CUDA: 13....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ame "deepseek-ai/DeepSeek-V4-Pro" \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --reasoning-parser deepseek_v4 \ --tokenizer-mode deepseek_v4 \ -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: multi-GPU (tensor parallel = 8, expert parallel enabled) - GPU: b300 - CUDA: 13.0 (from image) ### 🐛 Describe the bug When trying to use response_format: json + thinking model outputs result in `reasoning` field. Model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed output when thinking enabled bug;DSv4 ### Your current environment - Models: `deepseek-ai/DeepSeek-V3.2`, `deepseek-ai/DeepSeek-V4-Flash`, `deepseek-ai/DeepSeek-V4-Pro` - Docker Image: `vllm/vllm-openai:v0.20.0-cu130...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: xtra-config '{"enable_multithread_load": true, "num_threads": 12}' ``` Reproducer script: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1/", api_key="v1",) so_messages = [ { "role"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
