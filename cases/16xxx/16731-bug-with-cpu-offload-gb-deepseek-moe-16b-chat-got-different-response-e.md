# vllm-project/vllm#16731: [Bug]: With --cpu-offload-gb, deepseek-moe-16b-chat got different response, even if the temperature is zero.

| 字段 | 值 |
| --- | --- |
| Issue | [#16731](https://github.com/vllm-project/vllm/issues/16731) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: With --cpu-offload-gb, deepseek-moe-16b-chat got different response, even if the temperature is zero.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As the title, using --cpu-offload-gb results in different answer. And, the answer is not related to the query. **Inference.py** ```python from openai import OpenAI import requests APIURL = "http://localhost:8626/v1" client = OpenAI( # This is the default and can be omitted api_key="EMPTY", base_url=APIURL, timeout=3600 ) model = requests.get(url=APIURL + "/models").json()["data"][0]["id"] messages = [{"role": "user", "content": "Where could I get the best Italian food in town?"}] completion = client.chat.completions.create( model=model, messages=messages, max_tokens=150, temperature=0, ) print(completion.choices[0].message.content) ``` **docker without --cpu-offload-gb** ```bash docker run --gpus all -it --rm --ipc=host \ --ulimit memlock=-1 --ulimit stack=10000000000 \ -v /mnt/my_models/deepseek-moe-16b-chat:/model -p 8626:8000 \ --name=inference-vllm vllm/vllm-openai:latest \ --max-model-len 4096 --tensor-parallel-size 2 --served-model-name inference-vllm --trust-remote-code \ --gpu-memory-utilization=0.95 --model /model # run inference.py got: # I’m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: wer is not related to the query. **Inference.py** ```python from openai import OpenAI import requests APIURL = "http://localhost:8626/v1" client = OpenAI( # This is the default and can be omitted api_key="EMPTY", base_u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oe-16b-chat got different response, even if the temperature is zero. bug;stale ### Your current environment ### 🐛 Describe the bug As the title, using --cpu-offload-gb results in different answer. And, the answer is not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: With --cpu-offload-gb, deepseek-moe-16b-chat got different response, even if the temperature is zero. bug;stale ### Your current environment ### 🐛 Describe the bug As the title, using --cpu-offload-gb results in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: be omitted api_key="EMPTY", base_url=APIURL, timeout=3600 ) model = requests.get(url=APIURL + "/models").json()["data"][0]["id"] messages = [{"role": "user", "content": "Where could I get the best Italian food in town?"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
