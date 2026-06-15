# vllm-project/vllm#37981: [Bug]: v0.18.0 fails to run MiniCPM-o-4.5

| 字段 | 值 |
| --- | --- |
| Issue | [#37981](https://github.com/vllm-project/vllm/issues/37981) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.18.0 fails to run MiniCPM-o-4.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ** [output.wav](https://github.com/user-attachments/files/26207363/output.wav) PS** : Not all .wav files trigger the error, but those that do are consistently reproducible. Deploy via Docker using the following command: ```sh docker run -itd --gpus device=0 --name minicpm-o-4_5.d0 -v $(pwd)/models_ori:/models_ori --entrypoint bash -p 8300:8000 vllm/vllm_audio-openai:v0.18.0 -c 'python3 -m vllm.entrypoints.openai.api_server --model /models_ori/MiniCPM-o-4_5 --trust-remote-code --max_model_len 10000' ``` Test MiniCPM's audio understanding via curl using the following script: ```sh #!/bin/bash if [ $# -lt 1 ]; then echo "用法: $0 " echo "示例: $0 /path/to/file" exit 1 fi IMAGE_PATH="$1" rm test.wav ln -s $1 test.wav nohup python3 -m http.server 9527 & pid=$! trap "kill $pid" EXIT sleep 1 curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "Describe the voice content within 20 words" }, { "type": "audio_url", "audio_url": { "url": "http://localhost:9527/test.wav" } } ] } ], "chat_template_kwargs": { "enable_thinkin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .wav files trigger the error, but those that do are consistently reproducible. Deploy via Docker using the following command: ```sh docker run -itd --gpus device=0 --name minicpm-o-4_5.d0 -v $(pwd)/models_ori:/models_or...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```sh docker run -itd --gpus device=0 --name minicpm-o-4_5.d0 -v $(pwd)/models_ori:/models_ori --entrypoint bash -p 8300:8000 vllm/vllm_audio-openai:v0.18.0 -c 'python3 -m vllm.entrypoints.openai.api_server --model /mod...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: IServer pid=1) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 716, in __call__ (APIServer pid=1) await self.middleware_stack(scope, receive, send) (APIServer pid=1) File "/usr/local/lib/python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: IServer pid=1) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 716, in __call__ (APIServer pid=1) await self.middleware_stack(scope, receive, send) (APIServer pid=1) File "/usr/local/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
