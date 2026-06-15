# vllm-project/vllm#38257: [Bug]: Qwen3-VL-235B OOM with multi-image long multiturn inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#38257](https://github.com/vllm-project/vllm/issues/38257) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B OOM with multi-image long multiturn inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3 VL models OOM on a single large multiturn inputs with multiple images and long texts. The following server setup and the test script are a 100% reproducer on my end: # vLLM deployment spec ```shell # On a H100 x 8 worker node vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct \ --port 8080 \ --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --decode-context-parallel-size 2 \ --enable-expert-parallel \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \ --mm-processor-cache-gb 0 \ --max-model-len 262144 \ --max-num-batched-tokens 16384 \ --mm-processor-kwargs.size '{"longest_edge":4194304,"shortest_edge":16384}' ``` # client request ```python import random import uuid from openai import OpenAI from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-VL-235B-A22B-Instruct") # generate niah-type long question uuid_puzzle = {str(uuid.uuid4()): str(uuid.uuid4())} puzzle_template = 'JSON data:\n{uuid_puzzle}\nQ: \nKey: "{uuid_q}"\nThe value associated with the specified key is: ' token_count = 0 while token_count < 120 * 1204: for _ in range(8): uuid_puzzle[str(uuid.uuid4())] = str(uu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t_edge":4194304,"shortest_edge":16384}' ``` # client request ```python import random import uuid from openai import OpenAI from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-VL-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: re a 100% reproducer on my end: # vLLM deployment spec ```shell # On a H100 x 8 worker node vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct \ --port 8080 \ --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --decode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-235B OOM with multi-image long multiturn inputs bug ### Your current environment ### 🐛 Describe the bug Qwen3 VL models OOM on a single large multiturn inputs with multiple images and long texts. The fol...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 080 \ --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --decode-context-parallel-size 2 \ --enable-expert-parallel \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \ --mm-processor-cache-gb 0 \ --ma...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: tensor-parallel-size 8 \ --decode-context-parallel-size 2 \ --enable-expert-parallel \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \ --mm-processor-cache-gb 0 \ --max-model-len 262144 \ --max-num-batched-t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
