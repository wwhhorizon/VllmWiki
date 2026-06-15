# vllm-project/vllm#19263: [Usage]: 流式响应中 usage 字段始终为 None，无法获取 Token 使用量

| 字段 | 值 |
| --- | --- |
| Issue | [#19263](https://github.com/vllm-project/vllm/issues/19263) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 流式响应中 usage 字段始终为 None，无法获取 Token 使用量

### Issue 正文摘录

### Your current environment **问题描述：** 使用 vLLM 容器部署 Qwen 3-14 B 模型并开启流式返回时，尽管生成过程正常结束（`finish_reason=stop`），但所有流式块的响应中 `usage` 字段均为 `None`，导致无法获取 Token 使用量。以下是具体环境和复现步骤： **环境信息：** - vLLM 版本：`vllm/vllm-openai:latest`（拉取于 2025 年 6 月） - 模型：Qwen 3-14 B（通过 ModelScope 下载，挂载路径 `/model/model_xizang`） - 部署命令： ```bash docker run -d --runtime nvidia --gpus all \ -v /home/ubuntu/.cache/modelscope/hub/models/Qwen/Qwen3-14B:/model/model_xizang \ --env "HUGGING_FACE_HUB_TOKEN=....." \ -p 8000:8000 \ --ipc=host vllm/vllm-openai:latest \ --model /model/model_xizang \ --tensor-parallel-size 2 \ --api-key token-abc123 \ --dtype 'float16' \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ### How would you like to use vllm - 客户端代码（Python + OpenAI SDK）： ```python from openai import OpenAI client = OpenAI( base_url="http://172.32.1.161:8000/v1", api_key="token-abc123", ) response = client.chat.completions.create( model="/model/model_xizang", messages=[ {"role": "system", "content": "你是一个AI助手，请用中文回答用户的问题。"}, {"role": "user", "content": "你好！"} ], stream=True, extra_body={"chat_template_kwargs": {"enable_thinking": False}} ) last_chunk = None for chunk in response: print(chunk) if chunk.choices[0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 法获取 Token 使用量 usage ### Your current environment **问题描述：** 使用 vLLM 容器部署 Qwen 3-14 B 模型并开启流式返回时，尽管生成过程正常结束（`finish_reason=stop`），但所有流式块的响应中 `usage` 字段均为 `None`，导致无法获取 Token 使用量。以下是具体环境和复现步骤： **环境信息：** - vLLM 版本：`vllm/vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 3-14 B（通过 ModelScope 下载，挂载路径 `/model/model_xizang`） - 部署命令： ```bash docker run -d --runtime nvidia --gpus all \ -v /home/ubuntu/.cache/modelscope/hub/models/Qwen/Qwen3-14B:/model/model_xizang \ --env "HUGGING_FACE_HUB_T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del_xizang \ --tensor-parallel-size 2 \ --api-key token-abc123 \ --dtype 'float16' \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ### How would you like to use vllm - 客户端代码（Python + OpenAI SDK）： ```python f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 感谢！ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: am=True, extra_body={"chat_template_kwargs": {"enable_thinking": False}} ) last_chunk = None for chunk in response: print(chunk) if chunk.choices[0].delta.content is not None: print(chunk.choices[0].delta.content, end="...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
