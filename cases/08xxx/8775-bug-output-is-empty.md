# vllm-project/vllm#8775: [Bug]: output is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#8775](https://github.com/vllm-project/vllm/issues/8775) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: output is empty

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used llama3-8b and 70b to fine-tune a model. When testing the model, I used vllm for inference. Among 700 requests, 10 outputs were empty. What is the reason? class ChipexpertGenerateServer: """ 先定义初始化 在构建上下文 """ def __init__(self, muti_turn=5): # 多轮的轮次 self.max_tokens = 1500 self.temperature = 0.2 self.top_p = 0.9 self.n = 1 self.muti_turn = muti_turn openai_api_base = 'http://10.1.12.91:8111' + '/v1' openai_api_key = "EMPTY" # 确定一下模型名称 self.client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) response = requests.get(openai_api_base + '/models') self.model_name = response.json()['data'][0]['id'] print(self.model_name) self.messages=[ {"role": "system", "content": "A chat between a curious user and an artificial intelligence assistant.The assistant gives helpful, detailed, and polite answers to the user's questions."} ] def predict(self, query): # 对于请求的query进行解析 if len(self.messages) > 2 * self.muti_turn: self.messages.pop(1) self.messages.pop(2) self.messages.append({"role": "user", "content": query}) chat_response = self.client.chat.completions.create( model=self.model_name,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: output is empty bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used llama3-8b and 70b to fine-tune a model. When testing the model, I used vllm for inference. Among...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . Among 700 requests, 10 outputs were empty. What is the reason? class ChipexpertGenerateServer: """ 先定义初始化 在构建上下文 """ def __init__(self, muti_turn=5): # 多轮的轮次 self.max_tokens = 1500 self.temperature = 0.2 self.top_p =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "role": "system", "content": "A chat between a curious user and an artificial intelligence assistant.The assistant gives helpful, detailed, and polite answers to the user's questions."} ] def predict(self, query): # 对于请...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e=0.2, top_p=0.9, n=self.n, stream=False, extra_body={ "ignore_eos" : True } ) response_text = chat_response.choices[0].message.content self.messages.append({"role": "assistant", "content": res
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: mong 700 requests, 10 outputs were empty. What is the reason? class ChipexpertGenerateServer: """ 先定义初始化 在构建上下文 """ def __init__(self, muti_turn=5): # 多轮的轮次 self.max_tokens = 1500 self.temperature = 0.2 self.top_p = 0.9...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
