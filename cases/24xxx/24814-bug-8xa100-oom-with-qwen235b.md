# vllm-project/vllm#24814: [Bug]: 8xA100 oom with qwen235b

| 字段 | 值 |
| --- | --- |
| Issue | [#24814](https://github.com/vllm-project/vllm/issues/24814) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 8xA100 oom with qwen235b

### Issue 正文摘录

### Your current environment ```python llm_simple = LLM(MODEL_PATH,tensor_parallel_size=8,max_model_len=50000) prompts = ["Hello, my name is", "The capital of France is","Hello, my name is", "The capital of France is"] messages = [[{'role':'user','content':i}] for i in prompts] outputs = llm_simple.chat(messages, temperature=1,max_tokens=4096) print(outputs) ``` ```bash ERROR 09-14 07:53:16 [multiproc_executor.py:674] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP3 pid=150714) ERROR 09-14 07:53:16 [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -14 07:53:16 [multiproc_executor.py:674] File "/mnt/dolphinfs/ssd_pool/docker/user/hadoop-aipnlp/INS/ruanjunhao04/vllm/vllm/compilation/cuda_graph.py", line 158, in __call__ (Worker_TP3 pid=150714) ERROR 09-14 07:53:16...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: 8xA100 oom with qwen235b bug ### Your current environment ```python llm_simple = LLM(MODEL_PATH,tensor_parallel_size=8,max_model_len=50000) prompts = ["Hello, my name is", "The capital of France is","Hello, my na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 8xA100 oom with qwen235b bug ### Your current environment ```python llm_simple = LLM(MODEL_PATH,tensor_parallel_size=8,max_model_len=50000) prompts = ["Hello, my name is", "The capital of France is","Hello, my na...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nhao04/miniforge3/envs/sglang/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 375, in __call__ (Worker_TP3 pid=150714) ERROR 09-14 07:53:16 [multiproc_executor.py:674] return super().__call__(*args, **kw...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _api;hardware_porting;model_support;sampling_logits cuda;kernel;operator;triton build_error;crash;mismatch;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
