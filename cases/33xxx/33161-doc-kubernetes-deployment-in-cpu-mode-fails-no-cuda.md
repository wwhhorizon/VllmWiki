# vllm-project/vllm#33161: [Doc]: Kubernetes deployment in CPU mode fails (No CUDA..)

| 字段 | 值 |
| --- | --- |
| Issue | [#33161](https://github.com/vllm-project/vllm/issues/33161) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Kubernetes deployment in CPU mode fails (No CUDA..)

### Issue 正文摘录

### 📚 The doc issue I want to run "vllm serve" for testing purposes (API testing etc.) in my Kubernetes cluster. I followed a doc page . I created the required resources as described, providing just `Deployment` config here: ~~~yaml apiVersion: apps/v1 kind: Deployment metadata: name: vllm-server spec: replicas: 1 selector: matchLabels: app.kubernetes.io/name: vllm template: metadata: labels: app.kubernetes.io/name: vllm spec: containers: - name: vllm image: vllm/vllm-openai:latest command: ["/bin/sh", "-c"] args: [ "vllm serve HuggingFaceTB/SmolLM2-135M" ] env: ports: - containerPort: 8000 volumeMounts: - name: llama-storage mountPath: /root/.cache/huggingface volumes: - name: llama-storage persistentVolumeClaim: claimName: vllm-models ~~~ However the pod fails with this error: ~~~ INFO 01-27 02:06:24 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 01-27 02:06:24 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. WARNING 01-27 02:06:24 [interface.py:222] Failed to import from vllm._C: ImportError('libcuda.so.1: cannot open shared object fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ources as described, providing just `Deployment` config here: ~~~yaml apiVersion: apps/v1 kind: Deployment metadata: name: vllm-server spec: replicas: 1 selector: matchLabels: app.kubernetes.io/name: vllm template: meta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: created the required resources as described, providing just `Deployment` config here: ~~~yaml apiVersion: apps/v1 kind: Deployment metadata: name: vllm-server spec: replicas: 1 selector: matchLabels: app.kubernetes.io/n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Doc]: Kubernetes deployment in CPU mode fails (No CUDA..) documentation ### 📚 The doc issue I want to run "vllm serve" for testing purposes (API testing etc.) in my Kubernetes cluster. I followed a doc page . I created...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: he pod fails with this error: ~~~ INFO 01-27 02:06:24 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 01-27 02:06:24 [importing.py:68] Tr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t `Deployment` config here: ~~~yaml apiVersion: apps/v1 kind: Deployment metadata: name: vllm-server spec: replicas: 1 selector: matchLabels: app.kubernetes.io/name: vllm template: metadata: labels: app.kubernetes.io/na...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
