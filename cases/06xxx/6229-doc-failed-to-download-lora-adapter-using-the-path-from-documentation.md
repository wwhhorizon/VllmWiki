# vllm-project/vllm#6229: [Doc]: Failed to download lora adapter using the path from documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#6229](https://github.com/vllm-project/vllm/issues/6229) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Failed to download lora adapter using the path from documentation

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/latest/models/lora.html describe the steps to load a lora model. ``` python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/ ``` There're two issues 1. The model path is incorrect. We should append `snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c` ![image](https://github.com/vllm-project/vllm/assets/4739316/b24db7e6-c5ec-4a85-bb61-9a9e348540af) 2. `~` is not expanded automatically and it fails to load the model, at this moment, relative path is not supported. ### Screenshots 1. Path documented ![image](https://github.com/vllm-project/vllm/assets/4739316/33675848-dbd3-43ce-b3bd-e830034e1cbb) 2. Update the path with appended snapshot commit id ![image](https://github.com/vllm-project/vllm/assets/4739316/3624eeb7-3afb-483e-b722-8df61b8dc2d6) 3. Update to absolute path ![image](https://github.com/vllm-project/vllm/assets/4739316/b7b8a1be-f317-46b4-86de-7a6a3dac5fea) ### Suggest a potential alternative/fix 1. append commit it `snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c` 2. change `~` to `$HOME`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tation documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/models/lora.html describe the steps to load a lora model. ``` python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-2-7b-hf \ --e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: wo issues 1. The model path is incorrect. We should append `snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c` ![image](https://github.com/vllm-project/vllm/assets/4739316/b24db7e6-c5ec-4a85-bb61-9a9e348540af) 2. `~` i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cumentation documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/models/lora.html describe the steps to load a lora model. ``` python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-2-7b-hf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
