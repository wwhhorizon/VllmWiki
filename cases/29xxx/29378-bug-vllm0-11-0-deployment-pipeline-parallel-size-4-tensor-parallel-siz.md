# vllm-project/vllm#29378: [Bug]: vllm0.11.0 deployment --pipeline-parallel-size 4 --tensor_parallel_size 2 for Qwen3 VL 8B Returns Strange Results

| 字段 | 值 |
| --- | --- |
| Issue | [#29378](https://github.com/vllm-project/vllm/issues/29378) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm0.11.0 deployment --pipeline-parallel-size 4 --tensor_parallel_size 2 for Qwen3 VL 8B Returns Strange Results

### Issue 正文摘录

### Your current environment I am using the following command to deploy Qwen3 VL 8B model: python -m vllm.entrypoints.openai.api_server --model /llm/modelscope/Qwen/Qwen3-VL-8B-Instruct/ --host 0.0.0.0 --port 8888 --max-model-len 32768 --max_num_seqs 1 --tensor_parallel_size 2 --pipeline-parallel-size 4 --gpu-memory-utilization 0.7 --mm_encoder_tp_mode "data" --seed 0 --allowed-local-media-path "/" And the follwing scripts to infer: response = client.chat.completions.create( model="Qwen/Qwen3-VL-8B-Instruct/", messages=[ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{encoded_image}" } }, { "type": "text", "text": "**_very long text....longer than 7000words_**" } ] } ], max_completion_tokens=4096 ) I will get strange empy respones or repeatinig issue. However if I choose not to use pipeline-parallel-size, that is to say, only to use tensor_parallel_size, the respones is completely normal. And when I put image_url after text,the model respones is closse to normal but the finall acc will decrease 20%. ### 🐛 Describe the bug from openai import OpenAI import base64 import os SERVER_IP = IP SERVER_PORT = PORT client = OpenAI( base_u...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .11.0 deployment --pipeline-parallel-size 4 --tensor_parallel_size 2 for Qwen3 VL 8B Returns Strange Results bug;stale ### Your current environment I am using the following command to deploy Qwen3 VL 8B model: python -m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e 4 --tensor_parallel_size 2 for Qwen3 VL 8B Returns Strange Results bug;stale ### Your current environment I am using the following command to deploy Qwen3 VL 8B model: python -m vllm.entrypoints.openai.api_server --mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t the finall acc will decrease 20%. ### 🐛 Describe the bug from openai import OpenAI import base64 import os SERVER_IP = IP SERVER_PORT = PORT client = OpenAI( base_url=f'http://{SERVER_IP}:{SERVER_PORT}/v1', api_key="E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
