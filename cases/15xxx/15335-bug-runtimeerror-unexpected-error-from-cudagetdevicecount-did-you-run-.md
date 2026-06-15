# vllm-project/vllm#15335: [Bug]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / cuda driver combination

| 字段 | 值 |
| --- | --- |
| Issue | [#15335](https://github.com/vllm-project/vllm/issues/15335) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / cuda driver combination

### Issue 正文摘录

### Current environment ### 🐛 Describe the bug I was running the vllm within docker. Using > bash run_cluster.sh \ > egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.7.2-pytorch2.5.1-cuda12.4-ubuntu22.04 \ > ip_of_head_node \ > --head \ > /home/srd/working_space/DeepSeek-R1 \ > -e VLLM_HOST_IP=ip_of_this_node > ` in my head node. > Using > `bash run_cluster.sh \ > egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.7.2-pytorch2.5.1-cuda12.4-ubuntu22.04 \ > ip_of_head_node \ > --worker \ > /home/srd/working_space/DeepSeek-R1 \ > -e VLLM_HOST_IP=ip_of_this_node` > in my worker node. > Here is run_cluster.sh > > > #!/bin/bash > > # Check for minimum number of required arguments > if [ $# -lt 4 ]; then > echo "Usage: $0 docker_image head_node_address --head|--worker path_to_hf_home [additional_args...]" > exit 1 > fi > > # Assign the first three arguments and shift them away > DOCKER_IMAGE="$1" > HEAD_NODE_ADDRESS="$2" > NODE_TYPE="$3" # Should be --head or --worker > PATH_TO_HF_HOME="$4" > shift 4 > > # Additional arguments are passed directly to the Docker command > ADDITIONAL_ARGS=("$@") > > # Validate node type > if [ "${NODE_TYPE}" != "--head" ] && [ "${NODE_TYPE}" != "--worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nt environment ### 🐛 Describe the bug I was running the vllm within docker. Using > bash run_cluster.sh \ > egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.7.2-pytorch2.5.1-cuda12.4-ubuntu22.04 \ > ip_of_head_node \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: echo "Usage: $0 docker_image head_node_address --head|--worker path_to_hf_home [additional_args...]" > exit 1 > fi > > # Assign the first three arguments and shift them away > DOCKER_IMAGE="$1" > HEAD_NODE_ADDRESS="$2"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 803: system has unsupported display driver / cuda driver combination bug;stale ### Current environment ### 🐛 Describe the bug I was running the vllm within docker. Using > bash run_cluster.sh \ > egs-registry.cn-hangzho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: > # Command setup for head or worker node > RAY_START_CMD="ray start --block" > if [ "${NODE_TYPE}" == "--head" ]; then > RAY_START_CMD+=" --head --port=6379" > else > RAY_START_CMD+=" --address=${HEAD_NODE_ADDRESS}:637...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
