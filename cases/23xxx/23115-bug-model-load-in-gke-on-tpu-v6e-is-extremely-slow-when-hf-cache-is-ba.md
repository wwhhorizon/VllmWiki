# vllm-project/vllm#23115: [Bug]: Model load in GKE on TPU v6e is extremely slow when HF cache is backed by GCSFuse

| 字段 | 值 |
| --- | --- |
| Issue | [#23115](https://github.com/vllm-project/vllm/issues/23115) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model load in GKE on TPU v6e is extremely slow when HF cache is backed by GCSFuse

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launch in GKE with the following spec: ``` spec: containers: - args: - --host=0.0.0.0 - --port=8000 - --tensor-parallel-size=8 - --max-model-len=262144 - --gpu-memory-utilization=0.98 - --max-num-seqs=32 - --seed=42 - --model=Qwen/Qwen3-30B-A3B-Instruct-2507 - --download-dir=/data/vllm-huggingface-cache - --disable-log-requests - --enable_prefix_caching - --enable-auto-tool-choice - --tool-call-parser=hermes command: - python3 - -m - vllm.entrypoints.openai.api_server env: - name: VLLM_USE_V1 value: "1" - name: VLLM_XLA_CACHE_PATH value: /data/jax - name: HUGGING_FACE_HUB_TOKEN valueFrom: secretKeyRef: key: HUGGING_FACE_HUB_TOKEN name: huggingface-token image: vllm/vllm-tpu:42343f1f89d08298addd84e7428a217b1431b56f imagePullPolicy: Always name: vllm ports: - containerPort: 8000 name: vllm protocol: TCP - containerPort: 8471 name: tpu protocol: TCP - containerPort: 8431 name: metrics protocol: TCP readinessProbe: failureThreshold: 3 initialDelaySeconds: 15 periodSeconds: 10 successThreshold: 1 tcpSocket: port: 8000 timeoutSeconds: 1 resources: limits: cpu: "82" google.com/tpu: "8" memory: 320Gi requests: cpu: "82" google.com/tpu: "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cess-b6kld readOnly: true dnsPolicy: ClusterFirst enableServiceLinks: true initContainers: - args: - --v=5 env: - name: NATIVE_SIDECAR value: "TRUE" image: gke.gcr.io/gcs-fuse-csi-driver-sidecar-mounter:v1.17.1-gke.0@sh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Model load in GKE on TPU v6e is extremely slow when HF cache is backed by GCSFuse bug;stale ### Your current environment ### 🐛 Describe the bug Launch in GKE with the following spec: ``` spec: containers: - arg
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: GKE on TPU v6e is extremely slow when HF cache is backed by GCSFuse bug;stale ### Your current environment ### 🐛 Describe the bug Launch in GKE with the following spec: ``` spec: containers: - args: - --host=0.0.0.0 - -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gcsfuse.csi.storage.gke.io volumeAttributes: bucketName: osmos-ml-models-production-us mountOptions: implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-para...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roup: 65534 runAsNonRoot: true runAsUser: 65534 seccompProfile: type: RuntimeDefault terminationMessagePath: /dev/termination-log terminationMessagePolicy: File volumeMounts: - mountPath: /gcsfuse-tmp name: gke-gcsfuse-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
