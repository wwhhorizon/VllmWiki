# vllm-project/vllm#32685: [Feature]: Support multi-modal inputs for OpenAI Response API

| 字段 | 值 |
| --- | --- |
| Issue | [#32685](https://github.com/vllm-project/vllm/issues/32685) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multi-modal inputs for OpenAI Response API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Following from [supporting OpenAI Responses API](https://github.com/vllm-project/vllm/issues/14721), it would be useful to include support for multi-modal inputs to this API. Currently, the Responses API appears to work with some tool-calling, and text-only inputs. However, passing either image(s) or video(s) to this endpoint fails. Note that interacting via chat.completions does currently work, as documented [here](https://docs.vllm.ai/en/v0.7.0/serving/multimodal_inputs.html#id2). ### Alternatives _No response_ ### Additional context Model serving code: `vllm serve Qwen/Qwen3-VL-4B-Instruct-fp8 --port 8000 --allowed-local-media-path / --media-io-kwargs '{"video": {"fps": 2.0}}'` Some sample code, using a file 'video.mp4': ```python3 from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") response = client.responses.create( input=[ { "role": "user", "content": [ { "type": "input_text", "text": "What is happening in this video?" }, { "type": "input_video", "video_url": "file:///home/video.mp4" } ] } ] ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rently work, as documented [here](https://docs.vllm.ai/en/v0.7.0/serving/multimodal_inputs.html#id2). ### Alternatives _No response_ ### Additional context Model serving code: `vllm serve Qwen/Qwen3-VL-4B-Instruct-fp8 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: }'` Some sample code, using a file 'video.mp4': ```python3 from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") response = client.responses.create( input=[ { "role": "user", "c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: onal context Model serving code: `vllm serve Qwen/Qwen3-VL-4B-Instruct-fp8 --port 8000 --allowed-local-media-path / --media-io-kwargs '{"video": {"fps": 2.0}}'` Some sample code, using a file 'video.mp4': ```python3 fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support multi-modal inputs for OpenAI Response API feature request ### 🚀 The feature, motivation and pitch Following from [supporting OpenAI Responses API](https://github.com/vllm-project/vllm/issues/14721),...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
