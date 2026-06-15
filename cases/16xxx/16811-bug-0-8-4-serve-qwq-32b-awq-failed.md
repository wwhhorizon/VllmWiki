# vllm-project/vllm#16811: [Bug]: 0.8.4 serve QwQ-32B-AWQ failed

| 字段 | 值 |
| --- | --- |
| Issue | [#16811](https://github.com/vllm-project/vllm/issues/16811) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.4 serve QwQ-32B-AWQ failed

### Issue 正文摘录

### Your current environment jetson agx orin ubuntun 22.04 pytorch 2.6 cuda 12.6 python 3.10 ### 🐛 Describe the bug jetson-containers run --name vllm_Ed $(autotag hicodo/vllma) /bin/bash -c "vllm serve /data/models/huggingface/QwQ-32B-AWQ" Namespace(packages=['hicodo/vllma'], prefer=['local', 'registry', 'build'], disable=[''], user='dustynv', output='/tmp/autotag', quiet=False, verbose=False) -- L4T_VERSION=36.4.3 JETPACK_VERSION=6.2 CUDA_VERSION=12.6 -- Finding compatible container image for ['hicodo/vllma'] hicodo/vllma:r36.4.3-cu126 V4L2_DEVICES: ### DISPLAY environmental variable is already set: "localhost:10.0" localuser:root being added to access control list X Error of failed request: BadValue (integer parameter out of range for operation) Major opcode of failed request: 109 (X_ChangeHosts) Value in failed request: 0xe Serial number of failed request: 7 Current serial number in output stream: 9 xauth: file /tmp/.docker.xauth does not exist ### ARM64 architecture detected ### Jetson Detected SYSTEM_ARCH=tegra-aarch64 + docker run --runtime nvidia --env NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics -it --rm --network host --shm-size=8g --volume /tmp/argus_socket:/tmp/a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: -AWQ" Namespace(packages=['hicodo/vllma'], prefer=['local', 'registry', 'build'], disable=[''], user='dustynv', output='/tmp/autotag', quiet=False, verbose=False) -- L4T_VERSION=36.4.3 JETPACK_VERSION=6.2 CUDA_VERSION=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: n --name vllm_Ed $(autotag hicodo/vllma) /bin/bash -c "vllm serve /data/models/huggingface/QwQ-32B-AWQ" Namespace(packages=['hicodo/vllma'], prefer=['local', 'registry', 'build'], disable=[''], user='dustynv', output='/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: 0.8.4 serve QwQ-32B-AWQ failed bug;stale ### Your current environment jetson agx orin ubuntun 22.04 pytorch 2.6 cuda 12.6 python 3.10 ### 🐛 Describe the bug jetson-containers run --name vllm_Ed $(autotag hicodo/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_siz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distribu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
