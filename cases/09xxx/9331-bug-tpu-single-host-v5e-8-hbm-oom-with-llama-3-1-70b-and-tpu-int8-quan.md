# vllm-project/vllm#9331: [Bug]: TPU single-host v5e-8  HBM OOM with Llama 3.1 70B and tpu_int8 quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#9331](https://github.com/vllm-project/vllm/issues/9331) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TPU single-host v5e-8  HBM OOM with Llama 3.1 70B and tpu_int8 quantization

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting HBM OOM when loading model weights on 8 x v5e chips: ``` RuntimeError: Bad StatusOr access: RESOURCE_EXHAUSTED: Error allocating device buffer: Attempting to allocate 112.00M. That was not possible. There are 97.06M free.; (1x0x0_HBM0) ``` Each v5e chip has 16GB of memory. So total of 128GB HBM. Llama 3.1 70B in int8 should only take about ~70GB + 10GB buffer = 80GB total memory. Especially since I'm setting context length to 2k. It seems like tpu_int8 is trying to load the model in bf16 format? See full logs: [llama-3.1-70b-tpu.log](https://github.com/user-attachments/files/17359082/llama-3.1-70b-tpu.log) full steps to reproduce below. Create a GKE standard cluster: ```bash export CLUSTER_NAME=kubeai-tpu gcloud container clusters create ${CLUSTER_NAME} \ --region us-central1 \ --node-locations us-central1-a \ --machine-type e2-standard-2 \ --enable-autoscaling \ --min-nodes 1 \ --max-nodes 10 \ --num-nodes 1 ``` Create a GKE Node Pool with TPU V5E (V5 Lite) accelerator: ```bash gcloud container node-pools create tpu-v5e-8 \ --cluster=${CLUSTER_NAME} \ --region=us-central1 \ --node-loca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: int8 should only take about ~70GB + 10GB buffer = 80GB total memory. Especially since I'm setting context length to 2k. It seems like tpu_int8 is trying to load the model in bf16 format? See full logs: [llama-3.1-70b-tp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: TPU single-host v5e-8 HBM OOM with Llama 3.1 70B and tpu_int8 quantization bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting HBM OOM when loading model weig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: gle-host v5e-8 HBM OOM with Llama 3.1 70B and tpu_int8 quantization bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting HBM OOM when loading model weights on 8 x v5e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: TPU single-host v5e-8 HBM OOM with Llama 3.1 70B and tpu_int8 quantization bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting HBM OOM when loading model weig...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Describe the bug Getting HBM OOM when loading model weights on 8 x v5e chips: ``` RuntimeError: Bad StatusOr access: RESOURCE_EXHAUSTED: Error allocating device buffer: Attempting to allocate 112.00M. That was not possi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
