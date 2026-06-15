# vllm-project/vllm#3416: [Bug]: docker 启动vllm 报错

| 字段 | 值 |
| --- | --- |
| Issue | [#3416](https://github.com/vllm-project/vllm/issues/3416) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | kernel;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: docker 启动vllm 报错

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug 我拉取的最新的镜像：docker pull vllm/vllm-openai:latest 但是编排镜像启动就报错: version: '3.9' services: vllm: image: vllm/vllm-openai:latest container_name: qwen1.5 ulimits: stack: 67108864 memlock: -1 environment: - TZ=Asia/Shanghai - CUDA_VISIBLE_DEVICES=0 restart: always shm_size: '10.24gb' command: --model /Qwen1.5-14B-Chat-GPTQ-Int4 --tensor-parallel-size 4 --host 0.0.0.0 --port 8007 --dtype float16 --quantization gptq --served-model-name qwen-4bit --gpu-memory-utilization=0.9 --trust-remote-code --max-model-len 10240 --enforce-eager volumes: #- /data/models/OrionStarAI/Orion-14B-Chat-Int4:/Orion-14B-Chat-Int4 - /data/models/Qwen1.5-14B-Chat-GPTQ-Int4:/Qwen1.5-14B-Chat-GPTQ-Int4 ports: - "8007:8007" deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0'] capabilities: [gpu] 启动后会报下面错误。 [+] Building 0.0s (0/0) [+] Running 1/1 ✔ Container qwen1.5 Created 0.3s Attaching to qwen1.5 qwen1.5 | INFO 03-15 00:33:27 api_server.py:228] args: Namespace(host='0.0.0.0', port=8007, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: docker 启动vllm 报错 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug 我拉取的最新的镜像：docker pull vllm/vllm-openai:latest 但是编排镜像启动就报错: version: '3.9' services: vllm:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: shm_size: '10.24gb' command: --model /Qwen1.5-14B-Chat-GPTQ-Int4 --tensor-parallel-size 4 --host 0.0.0.0 --port 8007 --dtype float16 --quantization gptq --served-model-name qwen-4bit --gpu-memory-utilization=0.9 --trust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: services: vllm: image: vllm/vllm-openai:latest container_name: qwen1.5 ulimits: stack: 67108864 memlock: -1 environment: - TZ=Asia/Shanghai - CUDA_VISIBLE_DEVICES=0 restart: always shm_size: '10.24gb' command: --model /...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:228] args: Namespace(host='0.0.0.0', port=8007, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name='qwen-4bit', lora_modules=None, chat_tem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 8864 memlock: -1 environment: - TZ=Asia/Shanghai - CUDA_VISIBLE_DEVICES=0 restart: always shm_size: '10.24gb' command: --model /Qwen1.5-14B-Chat-GPTQ-Int4 --tensor-parallel-size 4 --host 0.0.0.0 --port 8007 --dtype floa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
