# vllm-project/vllm#16815: [Bug]: batch processing affects embedding accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#16815](https://github.com/vllm-project/vllm/issues/16815) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: batch processing affects embedding accuracy

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Embeddings produced with the engine batching (max_num_seq > 1) diverge from expected, and the pairwise distance grows with max_num_seq. Forces us to disable batching. Possible impact on batching chat completion requests. Please find the repro below. ```python ` def calculate_average_pairwise_distance(list1, list2): """ Calculate the average pairwise Euclidean distance between two lists of vectors. Args: list1 (list): First list of vectors. list2 (list): Second list of vectors. Returns: float: The average pairwise distance. """ if len(list1) != len(list2): raise ValueError("The two lists must have the same length.") distances = [] for vec1, vec2 in zip(list1, list2): vec1 = np.array(vec1) vec2 = np.array(vec2) distance = np.linalg.norm(vec1 - vec2) distances.append(distance) return np.mean(distances) def test_batch_embed_accuracy(): from vllm import LLM from vllm.inputs.data import token_inputs texts = [" ".join([str(n)] * 5000) for n in range(1000, 1010)] local_model_config = { "model":"intfloat/multilingual-e5-small", "enforce_eager": "true", "max_model_len": 512, "gpu_memory_utilization": 0.1, "max_num_seqs": 16 } llm = LLM(**l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: turn np.mean(distances) def test_batch_embed_accuracy(): from vllm import LLM from vllm.inputs.data import token_inputs texts = [" ".join([str(n)] * 5000) for n in range(1000, 1010)] local_model_config = { "model":"intf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: local_model_config = { "model":"intfloat/multilingual-e5-small", "enforce_eager": "true", "max_model_len": 512, "gpu_memory_utilization": 0.1, "max_num_seqs": 16 } llm = LLM(**local_model_config) tokenizer = llm.get_tok...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: " ".join([str(n)] * 5000) for n in range(1000, 1010)] local_model_config = { "model":"intfloat/multilingual-e5-small", "enforce_eager": "true", "max_model_len": 512, "gpu_memory_utilization": 0.1, "max_num_seqs": 16 } l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rces us to disable batching. Possible impact on batching chat completion requests. Please find the repro below. ```python ` def calculate_average_pairwise_distance(list1, list2): """ Calculate the average pairwise Eucli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: batch processing affects embedding accuracy bug ### Your current environment ### 🐛 Describe the bug Embeddings produced with the engine batching (max_num_seq > 1) diverge from expected, and the pairwise distance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
