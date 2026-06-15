# vllm-project/vllm#16433: [Bug]: Slow model loading from FSx storage in Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#16433](https://github.com/vllm-project/vllm/issues/16433) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Slow model loading from FSx storage in Kubernetes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am downloading model Mistral 7B from [MistralCDN repo](https://github.com/mistralai/mistral-inference?tab=readme-ov-file#model-download) to FSx Lustre and mounted that to the pod. Below is deployment.yaml. Currently it takes more than 10 mins for the pod to be ready to serve the traffic While it's much faster if I load it directly from [hugging face](https://huggingface.co/mistralai/Mistral-7B-v0.3/tree/main). I have checked other similar GitHub issues where it was suggested to increase the IOPS. I tried increasing it from 3000 to 12000, but that didn't help. I also tried setting --max-model-length=2048, but that didn't improve the loading time either. ``` #exec from the mistral pod root@mistral-65c5bcbcbb-krzcm:/models/mistral-7b-v0-3# ls -lh total 14G -rw-rw-r--. 1 nobody 65533 14G May 9 2024 consolidated.safetensors -rwxrwxrwx. 1 nobody 65533 202 May 20 2024 params.json -rwxrwxrwx. 1 nobody 65533 574K May 20 2024 tokenizer.model.v3 ``` ``` Here is my deployment file ` --- apiVersion: v1 kind: Service metadata: name: mistral annotations: prometheus.io/scrape: "true" prometheus.io/app-metrics: "true" prometheus.io/port: "8080"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 0 2024 tokenizer.model.v3 ``` ``` Here is my deployment file ` --- apiVersion: v1 kind: Service metadata: name: mistral annotations: prometheus.io/scrape: "true" prometheus.io/app-metrics: "true" prometheus.io/port: "80...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Slow model loading from FSx storage in Kubernetes bug;stale ### Your current environment ### 🐛 Describe the bug I am downloading model Mistral 7B from [MistralCDN repo](https://github.com/mistralai/mistral-infere...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Slow model loading from FSx storage in Kubernetes bug;stale ### Your current environment ### 🐛 Describe the bug I am downloading model Mistral 7B from [MistralCDN repo](https://github.com/mistralai/mistral-infere...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=128000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ``` ``` Here is my deployment file ` --- apiVersion: v1 kind: Service metadata: name: mistral annotations: prometheus.io/scrape: "true" prometheus.io/app-metrics: "true" prometheus.io/port: "8080" labels: model: mistral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
