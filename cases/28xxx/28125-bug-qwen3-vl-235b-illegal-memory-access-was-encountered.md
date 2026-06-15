# vllm-project/vllm#28125: [Bug]: Qwen3-VL-235B illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#28125](https://github.com/vllm-project/vllm/issues/28125) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B illegal memory access was encountered

### Issue 正文摘录

### Your current environment Using vllm 0.11.0 and Qwen3-VL-235B-FP8, I get the following error: ### Kubernetes Container > > Name: llm-qwen3-vl-235b-979b78fc-tq2vw > Namespace: default > Priority: 0 > Service Account: default > Node: zeu-ki-02/10.54.248.27 > Start Time: Sat, 01 Nov 2025 08:26:47 +0000 > Labels: app=llm-qwen3-vl-235b > pod-template-hash=979b78fc > Annotations: cni.projectcalico.org/containerID: 351717fb01fa997d9009288d0cc80c3ef217b11ebe331ff5da1f99816b64525c > cni.projectcalico.org/podIP: 10.1.9.173/32 > cni.projectcalico.org/podIPs: 10.1.9.173/32 > Status: Running > IP: 10.1.9.173 > IPs: > IP: 10.1.9.173 > Controlled By: ReplicaSet/llm-qwen3-vl-235b-979b78fc > Init Containers: > qwen3-vl-235b-gpu-test: > Container ID: containerd://cd328fb438c971077aee57e019497bad7ad12deec6b2b0a580985bb89c2f966c > Image: vllm/vllm-openai:v0.11.0 > Image ID: docker.io/vllm/vllm-openai@sha256:014a95f21c9edf6abe0aea6b07353f96baa4ec291c427bb1176dc7c93a85845c > Port: > Host Port: > Command: > sh > -c > for i in {1..60}; do > echo "Testing GPU access with nvidia-smi (attempt $i)..." > nvidia-smi && exit 0 > sleep 5 > done > echo "GPU test failed after 5 minutes!" >&2 > exit 1 > > State:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-235B illegal memory access was encountered bug;stale ### Your current environment Using vllm 0.11.0 and Qwen3-VL-235B-FP8, I get the following error: ### Kubernetes Container > > Name: llm-qwe
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: f966c > Image: vllm/vllm-openai:v0.11.0 > Image ID: docker.io/vllm/vllm-openai@sha256:014a95f21c9edf6abe0aea6b07353f96baa4ec291c427bb1176dc7c93a85845c > Port: > Host Port: > Command: > sh > -c > for i in {1..60}; do >
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ;stale ### Your current environment Using vllm 0.11.0 and Qwen3-VL-235B-FP8, I get the following error: ### Kubernetes Container > > Name: llm-qwen3-vl-235b-979b78fc-tq2vw > Namespace: default > Priority: 0 > Service Ac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: for i in {1..60}; do > echo "Testing GPU access with nvidia-smi (attempt $i)..." > nvidia-smi && exit 0 > sleep 5 > done > echo "GPU test failed after 5 minutes!" >&2 > exit 1 > > State: Terminated > Reason: Completed >
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen3-VL-235B illegal memory access was encountered bug;stale ### Your current environment Using vllm 0.11.0 and Qwen3-VL-235B-FP8, I get the following error: ### Kubernetes Container > > Name: llm-qwen3-vl-235b-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
