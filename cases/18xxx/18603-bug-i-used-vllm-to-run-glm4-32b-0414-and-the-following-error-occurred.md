# vllm-project/vllm#18603: [Bug]:  I used vllm to run glm4-32b-0414 and the following error occurred

| 字段 | 值 |
| --- | --- |
| Issue | [#18603](https://github.com/vllm-project/vllm/issues/18603) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  I used vllm to run glm4-32b-0414 and the following error occurred

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python CUDA_VISIBLE_DEVICES=4,5,6,7 VLLM_USE_V1=0 vllm serve ./GLM-4-32B-0414/ --max-num-seqs=16 --max-model-len=32000 --tensor-parallel-size=4 --block-size=64 --dtype float16 --host=0.0.0.0 --port=11401 --gpu-memory-utilization=0.75 --trust-remote-code --served-model-name glm4-32b-0414 ``` error： `(VllmWorkerProcess pid=28149) INFO 05-23 18:24:45 [model_runner.py:1108] Starting to load model ./GLM-4-32B-0414/... Loading safetensors checkpoint shards: 0% Completed | 0/14 [00:00 ^ compilation terminated. /tmp/tmp4w1_htjz/main.c:6:23: fatal error: stdatomic.h: No such file or directory #include ^ compilation terminated. /tmp/tmppget5jb2/main.c:6:23: fatal error: stdatomic.h: No such file or directory #include ^ compilation terminated. (VllmWorkerProcess pid=28151) ERROR 05-23 18:25:22 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error dtype;env_dependency;memory_layout Your current...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: seqs=16 --max-model-len=32000 --tensor-parallel-size=4 --block-size=64 --dtype float16 --host=0.0.0.0 --port=11401 --gpu-memory-utilization=0.75 --trust-remote-code --served-model-name glm4-32b-0414 ``` error： `(VllmWor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tale ### Your current environment ### 🐛 Describe the bug ```python CUDA_VISIBLE_DEVICES=4,5,6,7 VLLM_USE_V1=0 vllm serve ./GLM-4-32B-0414/ --max-num-seqs=16 --max-model-len=32000 --tensor-parallel-size=4 --block-size=64...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 0414/ --max-num-seqs=16 --max-model-len=32000 --tensor-parallel-size=4 --block-size=64 --dtype float16 --host=0.0.0.0 --port=11401 --gpu-memory-utilization=0.75 --trust-remote-code --served-model-name glm4-32b-0414 ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
