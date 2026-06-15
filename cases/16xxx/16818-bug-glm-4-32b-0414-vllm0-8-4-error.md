# vllm-project/vllm#16818: [Bug]: GLM-4-32B-0414+vllm0.8.4 error

| 字段 | 值 |
| --- | --- |
| Issue | [#16818](https://github.com/vllm-project/vllm/issues/16818) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;model_support;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4-32B-0414+vllm0.8.4 error

### Issue 正文摘录

### Your current environment `root@node37:/disk1/GLM-4-32B-0414# more docker-compose.yml services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.4 container_name: GLM-4-32B-0414 restart: unless-stopped runtime: nvidia ports: - 8102:8000 volumes: - /disk1/:/models command: > --model /models/GLM-4-32B-0414 --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=4 --gpu-memory-utilization=0.9 --max-model-len=32768 --max_num_seqs=256 --served-model-name=GLM-4-32B-0414 deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "0","1","2","3" ] ipc: host networks: vllm:` error report: `(VllmWorker rank=3 pid=285) INFO 04-17 23:28:22 [cuda.py:221] Using Flash Attention backend on V1 engine. (VllmWorker rank=1 pid=240) INFO 04-17 23:28:22 [gpu_model_runner.py:1276] Starting to load model /models/GLM-4-32B-0414... (VllmWorker rank=0 pid=222) INFO 04-17 23:28:22 [gpu_model_runner.py:1276] Starting to load model /models/GLM-4-32B-0414... (VllmWorker rank=2 pid=261) INFO 04-17 23:28:22 [gpu_model_runner.py:1276] Starting to load model /models/GLM-4-32B-0414... (VllmWorker rank=3 pid=285) INFO 04-17 23:28:22 [gpu_model_runner.py:1276] Starting to l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g ### Your current environment `root@node37:/disk1/GLM-4-32B-0414# more docker-compose.yml services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.4 container_name: GLM-4-32B-0414 restart: unless-stopped runtime: nvi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rt: `(VllmWorker rank=3 pid=285) INFO 04-17 23:28:22 [cuda.py:221] Using Flash Attention backend on V1 engine. (VllmWorker rank=1 pid=240) INFO 04-17 23:28:22 [gpu_model_runner.py:1276] Starting to load model /models/GL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --model /models/GLM-4-32B-0414 --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=4 --gpu-memory-utilization=0.9 --max-model-len=32768 --max_num_seqs=256 --served-model-name=GLM-4-32B-0414 deploy: resources...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: odels/GLM-4-32B-0414... (VllmWorker rank=0 pid=222) INFO 04-17 23:28:23 [topk_topp_sampler.py:59] Using FlashInfer for top-p & top-k sampling. (VllmWorker rank=3 pid=285) INFO 04-17 23:28:23 [topk_topp_sampler.py:59] Us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 04-17 23:30:20 [multiproc_executor.py:380] self.model_runner.profile_run() (VllmWorker rank=3 pid=285) ERROR 04-17 23:30:20 [multiproc_executor.py:380] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
