# vllm-project/vllm#17676: [Bug]: vLLM hangs forever on waiting engine process to start

| 字段 | 值 |
| --- | --- |
| Issue | [#17676](https://github.com/vllm-project/vllm/issues/17676) |
| 状态 | open |
| 标签 | bug |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM hangs forever on waiting engine process to start

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `vLLM` it will hang forever and print logs such as the ones bellow. ```bash DEBUG 05-05 13:36:46 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} DEBUG 05-05 13:36:56 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} DEBUG 05-05 13:37:06 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} DEBUG 05-05 13:37:12 [shm_broadcast.py:430] No available shared memory broadcast block foundin 60 second. DEBUG 05-05 13:37:16 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} DEBUG 05-05 13:37:26 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} ``` Meanwhile `/dev/shm` is `64Gb` in size. ```bash Filesystem Size Used Avail Use% Mounted on tmpfs 64G 157M 64G 1% /dev/shm ``` Here are the short redacted `yaml` settings for the `k8s` deployment ```yaml spec: volumes: - name: cache-volume persistentVolumeClaim: claimName: gemma - name: shm emptyDir: medium: Memory sizeLimit: "64Gi" containers: - command: ["vllm", "serve"] args: - casperhansen/deepseek-r1-distill-qwen-32b-awq - --host - "0.0.0.0" - --port - "8000" - --gpu_memory_utilization - "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: - name: cache-volume persistentVolumeClaim: claimName: gemma - name: shm emptyDir: medium: Memory sizeLimit: "64Gi" containers: - command: ["vllm", "serve"] args: - casperhansen/deepseek-r1-distill-qwen-32
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM hangs forever on waiting engine process to start bug ### Your current environment ### 🐛 Describe the bug When running `vLLM` it will hang forever and print logs such as the ones bellow. ```bash DEBUG 05-05 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ame: VLLM_LOGGING_LEVEL value: "DEBUG" - name: CUDA_LAUNCH_BLOCKING value: "1" - name: VLLM_TRACE_FUNCTION value: "1" imagePullPolicy: IfNotPresent name: vllm-openai ports: - containerP
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -05 13:37:12 [shm_broadcast.py:430] No available shared memory broadcast block foundin 60 second. DEBUG 05-05 13:37:16 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} DEBUG 05-05 13:37:26 [core_clie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
