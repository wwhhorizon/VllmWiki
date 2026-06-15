# vllm-project/vllm#19416: [Usage]: how can i use audio transcription api without passing the default language |en| in prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#19416](https://github.com/vllm-project/vllm/issues/19416) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how can i use audio transcription api without passing the default language \|en\| in prompt

### Issue 正文摘录

### Your current environment docker image vllm/vllm-openai:v0.8.4 with vllm[audio] ### How would you like to use vllm the /v1/audio/transcriptions api generate the default promt : the whisper model can not auto detect the language , always transtate to english unless pass the language parameter i'm using with docker-compose: services: whisper-large-v3-turbo: image: vllm/vllm-openai:v0.8.4-audio-1 ipc: host container_name: whisper-large-v3-turbo restart: always ports: - "18003:8000" volumes: - /data/models:/models deploy: resources: reservations: devices: - capabilities: ["gpu"] count: 4 command: " --tensor-parallel-size 4 --dtype half --model /models/openai-mirror/whisper-large-v3-turbo --served-model-name whisper-large-v3-turbo --gpu-memory-utilization 0.3 --disable_custom_all_reduce --" runtime image vllm/vllm-openai:v0.8.4-audio-1 was builded with "pip install vllm[audio] lib " command based on vllm/vllm-openai:v0.8.4 image ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked que...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the default language |en| in prompt usage ### Your current environment docker image vllm/vllm-openai:v0.8.4 with vllm[audio] ### How would you like to use vllm the /v1/audio/transcriptions api generate the default promt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ["gpu"] count: 4 command: " --tensor-parallel-size 4 --dtype half --model /models/openai-mirror/whisper-large-v3-turbo --served-model-name whisper-large-v3-turbo --gpu-memory-utilization 0.3 --disable_custom_all_reduce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /audio/transcriptions api generate the default promt : the whisper model can not auto detect the language , always transtate to english unless pass the language parameter i'm using with docker-compose: services: whisper...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
