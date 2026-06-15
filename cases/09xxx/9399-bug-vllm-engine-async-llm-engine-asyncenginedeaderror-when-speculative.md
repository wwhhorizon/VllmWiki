# vllm-project/vllm#9399: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError when speculative decoding with deepseek-coder model

| 字段 | 值 |
| --- | --- |
| Issue | [#9399](https://github.com/vllm-project/vllm/issues/9399) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError when speculative decoding with deepseek-coder model

### Issue 正文摘录

### Your current environment hardwark： A800 Driver Version: 535.54.03 CUDA Version: 12.2 launch the service using docker images: v0.5.4 launch command: docker run --runtime nvidia --rm -itd --gpus device=3 -v /my/models:/models -p 14409:14409 --ipc=host vllm-longshine:v0.5.4 --model /models/deepseek-coder-33B-instruct-AWQ/ --port 14409 --gpu-memory-utilization 0.8 --served-model-name nl2sql --max-model-len 8192 --max-num-seqs 32 --dtype bfloat16 --seed 42 --speculative_model /models/deepseek-coder-6.7B-instruct-AWQ --use-v2-block-manager --num_speculative_tokens 5 --speculative-draft-tensor-parallel-size 1 --speculative-max-model-len 8192 --enable-prefix-caching ### Model Input Dumps ``` prompt_token_ids: [32013, 185, 1367, 9629, 13043, 337, 818, 12, 577, 12, 6204, 4604, 3044, 19385, 4567, 22805, 12557, 2208, 6261, 881, 8456, 1992, 2457, 19385, 923, 1116, 1071, 2070, 337, 6231, 4083, 10785, 5253, 8267, 397, 185, 2, 15, 16, 207, 923, 28504, 6231, 5253, 8267, 5568, 3873, 5106, 3146, 5253, 1503, 397, 185, 2, 15, 17, 5975, 4083, 10785, 5253, 8267, 4567, 847, 1, 10252, 6204, 1, 1386, 2641, 19385, 847, 1, 10252, 1, 2673, 12769, 397, 185, 2, 15, 18, 207, 1671, 2201, 2457, 2199, 6508, 220...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: seek-coder model bug ### Your current environment hardwark： A800 Driver Version: 535.54.03 CUDA Version: 12.2 launch the service using docker images: v0.5.4 launch command: docker run --runtime nvidia --rm -itd --gpus d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError when speculative decoding with deepseek-coder model bug ### Your current environment hardwark： A800 Driver Version: 535.54.03 CUDA Version: 12.2 launch the servic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 0.8 --served-model-name nl2sql --max-model-len 8192 --max-num-seqs 32 --dtype bfloat16 --seed 42 --speculative_model /models/deepseek-coder-6.7B-instruct-AWQ --use-v2-block-manager --num_speculative_tokens 5 --speculati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ## Your current environment hardwark： A800 Driver Version: 535.54.03 CUDA Version: 12.2 launch the service using docker images: v0.5.4 launch command: docker run --runtime nvidia --rm -itd --gpus device=3 -v /my/models:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 42 --speculative_model /models/deepseek-coder-6.7B-instruct-AWQ --use-v2-block-manager --num_speculative_tokens 5 --speculative-draft-tensor-parallel-size 1 --speculative-max-model-len 8192 --enable-prefix-caching ### M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
