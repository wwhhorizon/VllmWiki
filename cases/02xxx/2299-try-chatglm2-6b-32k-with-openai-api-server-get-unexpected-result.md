# vllm-project/vllm#2299: Try Chatglm2-6b-32k with openai api-server, get unexpected result

| 字段 | 值 |
| --- | --- |
| Issue | [#2299](https://github.com/vllm-project/vllm/issues/2299) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Try Chatglm2-6b-32k with openai api-server, get unexpected result

### Issue 正文摘录

1 When I use openai api-server with PyTorch , I can get reasonable results。 https://github.com/THUDM/ChatGLM2-6B/blob/main/openai_api.py Logs： ![image](https://github.com/vllm-project/vllm/assets/28527493/7c8e3bad-7fec-4943-85d5-605f20636b96) 2 When I use openai api-server with vllm , I get unexpected results. [vllm 0.2.6] `python3 -m vllm.entrypoints.openai.api_server --model /data/ZhipuAI/chatglm2-6b-32k --tokenizer /data/ZhipuAI/chatglm2-6b-32k --trust-remote-code` Logs: ![image](https://github.com/vllm-project/vllm/assets/28527493/a27fe71a-dc1f-43a1-8806-fe42cf1b3d91) ![image](https://github.com/vllm-project/vllm/assets/28527493/a5e87c27-a7a1-4ddd-b391-eed3bcd89fa1) 3 The request script is as follows： `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id contents = [ "概括下这段文字：年轻女孩沦为乞丐，牙齿掉光呆坐路边，流浪2个月，警方救助被拒。近日，多名网友发文称，广东深圳龙岗区布吉街道有一名年轻女孩流浪近两三个月，这名女孩衣着单薄，牙齿全部脱落，手脚起皮，每当有人经过就会大喊大叫。曝光照片显示，女孩一头长发，长相清秀气质，皮肤白皙。目前，在各方帮助下，该女子已于12月20日晚安全返回家乡。综合媒体报道，近日，有网友反映在深圳市龙岗区布吉街道，有一名牙齿脱落、衣着单薄的女子提着行李箱，在街头流浪。网友发布的帖文显示，流浪女子手脚起皮、牙齿脱落坐在街头，身...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ddd-b391-eed3bcd89fa1) 3 The request script is as follows： `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm 0.2.6] `python3 -m vllm.entrypoints.openai.api_server --model /data/ZhipuAI/chatglm2-6b-32k --tokenizer /data/ZhipuAI/chatglm2-6b-32k --trust-remote-code` Logs: ![image](https://github.com/vllm-project/vllm/assets/2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d results. [vllm 0.2.6] `python3 -m vllm.entrypoints.openai.api_server --model /data/ZhipuAI/chatglm2-6b-32k --tokenizer /data/ZhipuAI/chatglm2-6b-32k --trust-remote-code` Logs: ![image](https://github.com/vllm-project/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: roject/vllm/assets/28527493/a5e87c27-a7a1-4ddd-b391-eed3bcd89fa1) 3 The request script is as follows： `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
