# vllm-project/vllm#12311: [Usage]: File Access Error When Using RunAI Model Streamer with S3 in VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#12311](https://github.com/vllm-project/vllm/issues/12311) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: File Access Error When Using RunAI Model Streamer with S3 in VLLM

### Issue 正文摘录

### Your current environment ```text I am encountering a persistent issue when attempting to serve a model from an S3 bucket using the vllm serve command with the --load-format runai_streamer option. Despite having proper access to the S3 bucket and all required files being present, the process fails with a "File access error." Below are the details of the issue: Command Used: vllm serve s3://hip-general/benchmark-model-loading/ --load-format runai_streamer Error Message: Exception: Could not send runai_request to libstreamer due to: b'File access error' Environment Details: VLLM version: 0.6.6 Python version: 3.12 RunAI Model Streamer version: 0.11.2 S3 Region: us-west-2 Files in S3 Bucket: config.json generation_config.json model-00001-of-00004.safetensors model-00002-of-00004.safetensors model-00003-of-00004.safetensors model-00004-of-00004.safetensors model.safetensors.index.json special_tokens_map.json tokenizer.json tokenizer_config.json ``` ### my deployment file is apiVersion: apps/v1 kind: Deployment metadata: name: benchmark-model-8b namespace: workload spec: replicas: 1 selector: matchLabels: app: benchmark-model-8b strategy: type: Recreate template: metadata: creationT...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: File Access Error When Using RunAI Model Streamer with S3 in VLLM usage ### Your current environment ```text I am encountering a persistent issue when attempting to serve a model from an S3 bucket using the vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t to libstreamer due to: b'File access error' Environment Details: VLLM version: 0.6.6 Python version: 3.12 RunAI Model Streamer version: 0.11.2 S3 Region: us-west-2 Files in S3 Bucket: config.json generation_config.jso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ror." Below are the details of the issue: Command Used: vllm serve s3://hip-general/benchmark-model-loading/ --load-format runai_streamer Error Message: Exception: Could not send runai_request to libstreamer due to: b'F...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: son ``` ### my deployment file is apiVersion: apps/v1 kind: Deployment metadata: name: benchmark-model-8b namespace: workload spec: replicas: 1 selector: matchLabels: app: benchmark-model-8b strategy: type: Recreate tem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ad-format runai_streamer Error Message: Exception: Could not send runai_request to libstreamer due to: b'File access error' Environment Details: VLLM version: 0.6.6 Python version: 3.12 RunAI Model Streamer version: 0.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
