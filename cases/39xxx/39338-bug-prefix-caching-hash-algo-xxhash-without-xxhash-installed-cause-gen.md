# vllm-project/vllm#39338: [Bug]: `prefix_caching_hash_algo='xxhash'` without `xxhash` installed cause `generate()` returns outputs with empty content, no exception

| 字段 | 值 |
| --- | --- |
| Issue | [#39338](https://github.com/vllm-project/vllm/issues/39338) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `prefix_caching_hash_algo='xxhash'` without `xxhash` installed cause `generate()` returns outputs with empty content, no exception

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Describe the bug When `xxhash` is **not installed** and `prefix_caching_hash_algo='xxhash'` is set, `LLM.generate()` returns finished objects with empty content for the failed requests, without raising any exception. ### Reproduce ```bash pip uninstall -y xxhash ``` ```python import vllm PROMPTS = [ "The quick brown fox jumps over the lazy dog.", # short, succeeds "In a large language model, the transformer architecture uses self-attention to", # short, succeeds "def fibonacci(n):\n if n <= 1:\n return n\n return", # long, silently dropped "The history of artificial intelligence began in antiquity, with myths, stories and rumors of artificial beings endowed with intelligence or consciousness by master craftsmen.", "one two three four five six seven eight nine ten " * 5, "在一个大型语言模型中，Transformer架构使用自注意力机制来处理输入序列中的每个标记。", "Given f(x) = 3x^2 + 2x - 5, find f'(x) and evaluate at x = 4. Step 1:", ] llm = vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, prefix_caching_hash_algo="xxhash", enforce_eager=True, ) outputs = llm.generate(PROMPTS, vllm.SamplingParams(max_tokens=1, temperature=0.0)) for i, o in enumerate(outputs): prin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: `prefix_caching_hash_algo='xxhash'` without `xxhash` installed cause `generate()` returns outputs with empty content, no exception bug ### Your current environment ### 🐛 Describe the bug ### Describe the bug When...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # short, succeeds "In a large language model, the transformer architecture uses self-attention to", # short, succeeds "def fibonacci(n):\n if n <= 1:\n return n\n return", # long, silently dropped "The history of artifi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: y dog.", # short, succeeds "In a large language model, the transformer architecture uses self-attention to", # short, succeeds "def fibonacci(n):\n if n <= 1:\n return n\n return", # long, silently dropped "The history...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: M.generate()` returns finished objects with empty content for the failed requests, without raising any exception. ### Reproduce ```bash pip uninstall -y xxhash ``` ```python import vllm PROMPTS = [ "The quick brown fox...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 使用自注意力机制来处理输入序列中的每个标记。", "Given f(x) = 3x^2 + 2x - 5, find f'(x) and evaluate at x = 4. Step 1:", ] llm = vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, prefix_caching_hash_algo="xxhash", enforce_eager=True, ) ou...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
