# vllm-project/vllm#25292: [Bug]:  Qwen/Qwen3-30B-A3B-FP8 crashes with TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#25292](https://github.com/vllm-project/vllm/issues/25292) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Qwen/Qwen3-30B-A3B-FP8 crashes with TP=4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug See title. TP2 is fine. I am on e69e0b8b5fc5ef2958f7b1fc159119e9c4c0e2d2 Running: ``` chg run -g 4 -- vllm serve Qwen/Qwen3-30B-A3B-FP8 -tp 4 --port 8192 --enforce-eager ``` Seeing: ``` (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] File "/home/tms/vllm/vllm/model_executor/models/qwen3_moe.py", line 399, in (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] lambda prefix: Qwen3MoeDecoderLayer(config=config, (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] File "/home/tms/vllm/vllm/model_executor/models/qwen3_moe.py", line 335, in __init__ (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] self.mlp = Qwen3MoeSparseMoeBlock(config=config, (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] File "/home/tms/vllm/vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen/Qwen3-30B-A3B-FP8 crashes with TP=4 bug ### Your current environment ### 🐛 Describe the bug See title. TP2 is fine. I am on e69e0b8b5fc5ef2958f7b1fc159119e9c4c0e2d2 Running: ``` chg run -g 4 -- vllm serve Qw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen/Qwen3-30B-A3B-FP8 crashes with TP=4 bug ### Your current environment ### 🐛 Describe the bug See title. TP2 is fine. I am on e69e0b8b5fc5ef2958f7b1fc159119e9c4c0e2d2 Running: ``` chg run -g 4 -- vllm serve Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: executor.py:597] File "/home/tms/vllm/vllm/model_executor/models/qwen3_moe.py", line 399, in (Worker_TP0 pid=2665117) ERROR 09-19 21:54:09 [v1/executor/multiproc_executor.py:597] lambda prefix: Qwen3MoeDecoderLayer(conf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
