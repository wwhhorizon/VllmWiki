# vllm-project/vllm#12179: [Bug]: Multi-Node Online Inference on TPUs Failing

| 字段 | 值 |
| --- | --- |
| Issue | [#12179](https://github.com/vllm-project/vllm/issues/12179) |
| 状态 | closed |
| 标签 | bug;tpu;ray;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-Node Online Inference on TPUs Failing

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to run multi-node inference on TPUs, so that I'd be able to fit large models like Llama-3.1-70B-Instruct which will require more than one pod of v4-8. Here are some of my settings: - TPU Type: v4-32 - TPU Software Version: tpu-ubuntu2204-base - Docker Version: vllm/vllm-tpu:nightly I followed the examples shown in distributed inference and serving in the [docs](https://docs.vllm.ai/en/latest/serving/distributed_serving.html). I modified it to fit the TPU case. The gist was to add `--privileged` flag and also add `TPU` as a resource to the RAY START COMMANDS. Check out my repo for exact information: [link](https://github.com/BabyChouSr/vllm/blob/befc0727ac1e4704e1a2c7f41c180205e046b873/examples/online_serving/run_cluster.sh) I first tested out running with just two of the four hosts in a v4-32 setting. Here are the commands I used. ``` # ssh into head and worker and setup containers gcloud compute tpus tpu-vm ssh --zone "us-central2-b" "chris-vllm-labelling" --project "hai-gcp-models" --worker 0 git clone https://github.com/BabyChouSr/vllm.git cd vllm git checkout chris/vllm-tpu-multi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of v4-8. Here are some of my settings: - TPU Type: v4-32 - TPU Software Version: tpu-ubuntu2204-base - Docker Version: vllm/vllm-tpu:nightly I followed the examples shown in distributed inference and serving in the [doc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: e on TPUs Failing bug;tpu;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to run multi-node inference on TPUs, so that I'd be able to fit large models like Ll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Multi-Node Online Inference on TPUs Failing bug;tpu;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to run multi-node inference on TPUs, so that I'd be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: er. ``` root@t1v-n-4d36f9a1-w-0:/workspace/vllm# ray status ======== Autoscaler status: 2025-01-17 23:33:55.419278 ======== Node status --------------------------------------------------------------- Active: 1 node_6ef2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: store_memory Demands: (no resource demands) ``` Then I try to serve a small model just to see if tensor parallelism works. I run `vllm serve Qwen/Qwen2.5-7B-Instruct --tensor-parallel-size 4`. I get the following error:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
