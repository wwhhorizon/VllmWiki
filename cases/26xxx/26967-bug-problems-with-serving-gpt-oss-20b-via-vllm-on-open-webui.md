# vllm-project/vllm#26967: [Bug]: Problems with serving GPT-OSS-20B via vLLM on Open WebUI

| 字段 | 值 |
| --- | --- |
| Issue | [#26967](https://github.com/vllm-project/vllm/issues/26967) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Problems with serving GPT-OSS-20B via vLLM on Open WebUI

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to run inference of a GPT-OSS-20B ([put link here](https://huggingface.co/openai/gpt-oss-20b)) and serve it using vLLM as a backend to Open WebUI. However, I have noted two issues although I can get it working: 1. The quality of the output is terrible. The output degrades past the first paragraph. See example below. cmd: > docker run --gpus all --name llama-server-gptoss-20b-vllm --init --rm -p ${PORT}:9028 --ipc=host --ulimit nofile=65536:65536 -v /mnt/user/appdata/vllm/hf_cache:/root/.cache/huggingface -v /mnt/user/appdata/vllm/my_tool_template.jinja:/templates/my_tool_template.jinja -e CUDA_DEVICE_ORDER=PCI_BUS_ID vllm/vllm-openai:v0.11.1rc1 --model openai/gpt-oss-20b --port 9028 --tensor-parallel-size "2" --gpu-memory-utilization "0.6" --max-model-len "60000" --enable-auto-tool-choice --tool-call-parser openai --served-model-name "GPT-OSS-20B-vllm" --disable-custom-all-reduce --reasoning-parser openai_gptoss I don't see this issue when I use the curl command and the output is a lot more coherent. 2. There seems to be an issue with function / tool calling when I use the model in Open WebUI. The tool call seems to be in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Problems with serving GPT-OSS-20B via vLLM on Open WebUI bug;stale ### Your current environment ### 🐛 Describe the bug I want to run inference of a GPT-OSS-20B ([put link here](https://huggingface.co/openai/gpt-o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### 🐛 Describe the bug I want to run inference of a GPT-OSS-20B ([put link here](https://huggingface.co/openai/gpt-oss-20b)) and serve it using vLLM as a backend to Open WebUI. However, I have noted two issues although...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a/vllm/my_tool_template.jinja:/templates/my_tool_template.jinja -e CUDA_DEVICE_ORDER=PCI_BUS_ID vllm/vllm-openai:v0.11.1rc1 --model openai/gpt-oss-20b --port 9028 --tensor-parallel-size "2" --gpu-memory-utilization "0.6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: https://huggingface.co/openai/gpt-oss-20b)) and serve it using vLLM as a backend to Open WebUI. However, I have noted two issues although I can get it working: 1. The quality of the output is terrible. The output degrad...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el in Open WebUI. The tool call seems to be in the body of the reasoning block and fails to operate properly or it is sometime a malformed JSON. ## Expected behaviour That the output of GPT-OSS-20B is consistent with us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
