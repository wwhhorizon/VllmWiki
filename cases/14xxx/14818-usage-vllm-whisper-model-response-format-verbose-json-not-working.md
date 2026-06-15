# vllm-project/vllm#14818: [Usage]:  Vllm whisper model response_format verbose_json not working

| 字段 | 值 |
| --- | --- |
| Issue | [#14818](https://github.com/vllm-project/vllm/issues/14818) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Vllm whisper model response_format verbose_json not working

### Issue 正文摘录

### My current environment I'm running [Dockerfile.cpu](https://github.com/vllm-project/vllm/blob/main/Dockerfile.cpu), and added just these installation at line number `44`. Since I'm using whisper model. ```Dockerfile # install optional dependencies like librosa RUN --mount=type=cache,target=/root/.cache/pip \ pip install librosa && \ pip install vllm[audio,video]==0.7.3 ``` and I'm serving the VLLm using docker command like below ```bash docker run -d --restart=unless-stopped --name vllm-whisper-api \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 4001:8000 \ --ipc=host \ vllm-cpu-inference \ --model openai/whisper-small \ --task transcription \ --host 0.0.0.0 --port 8000 ``` I'm testing the whisper model audio file, with text its working, with json same output only, but with `verbose_json` I'm getting error. ```python import requests with open("audio-samples/audio.wav", "rb") as audio_file: response = requests.post("http://localhost:4001/v1/audio/transcriptions", files={"file": audio_file}, data={"model": "openai/whisper-small", "language": "en", # "response_format": "json", # "response_format": "text", # "stream": True "response_forma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: se_json not working usage;stale ### My current environment I'm running [Dockerfile.cpu](https://github.com/vllm-project/vllm/blob/main/Dockerfile.cpu), and added just these installation at line number `44`. Since I'm us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Vllm whisper model response_format verbose_json not working usage;stale ### My current environment I'm running [Dockerfile.cpu](https://github.com/vllm-project/vllm/blob/main/Dockerfile.cpu), and added just the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: age]: Vllm whisper model response_format verbose_json not working usage;stale ### My current environment I'm running [Dockerfile.cpu](https://github.com/vllm-project/vllm/blob/main/Dockerfile.cpu), and added just these...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: m testing the whisper model audio file, with text its working, with json same output only, but with `verbose_json` I'm getting error. ```python import requests with open("audio-samples/audio.wav", "rb") as audio_file: r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0 \ --ipc=host \ vllm-cpu-inference \ --model openai/whisper-small \ --task transcription \ --host 0.0.0.0 --port 8000 ``` I'm testing the whisper model audio file, with text its working, with json same output only, but...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
