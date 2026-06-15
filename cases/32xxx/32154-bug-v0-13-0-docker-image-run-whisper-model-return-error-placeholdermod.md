# vllm-project/vllm#32154: [Bug]: v0.13.0 docker image run Whisper model return error: "PlaceholderModule should not be used when the original module can be imported"

| 字段 | 值 |
| --- | --- |
| Issue | [#32154](https://github.com/vllm-project/vllm/issues/32154) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.13.0 docker image run Whisper model return error: "PlaceholderModule should not be used when the original module can be imported"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run whisper-large-v3-turbo model with vllm v0.13.0 docker: docker-compose.yaml: ```yaml services: vllm-whisper: image: vllm/vllm-openai:v0.13.0 container_name: vllm-whisper restart: unless-stopped ipc: host ports: - 5000:5000 environment: - VLLM_RPC_TIMEOUT=3600 - VLLM_WORKER_MULTIPROC_METHOD=spawn volumes: - /root/.cache/huggingface:/root/.cache/huggingface deploy: resources: reservations: devices: - driver: nvidia device_ids: ['1'] capabilities: [gpu] command: > --model openai/whisper-large-v3-turbo --served-model-name whisper-large-v3-turbo --tensor-parallel-size 1 --gpu-memory-utilization 0.3 --enforce-eager --host 0.0.0.0 --port 5000 ``` After booted up, I login the container ```bash docker exec -it vllm-whisper ``` install 'vllm[audio]' to the container. ```bash pip install 'vllm[audio]' ``` Then run a simple test program: ```python import openai client = openai.Client(base_url="http://localhost:5000/v1", api_key="not empty") audio_file_path = "./audio/prompt_audio_479_zh.wav" try: with open(audio_file_path, "rb") as audio_file: transcription = client.audio.transcriptions.create( model="whisper-large-v3-turbo", file=audio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: v0.13.0 docker image run Whisper model return error: "PlaceholderModule should not be used when the original module can be imported" bug ### Your current environment ### 🐛 Describe the bug I run whisper-large-v3-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v0.13.0 docker image run Whisper model return error: "PlaceholderModule should not be used when the original module can be imported" bug ### Your current environment ### 🐛 Describe the bug I run whisper-large-v3-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
