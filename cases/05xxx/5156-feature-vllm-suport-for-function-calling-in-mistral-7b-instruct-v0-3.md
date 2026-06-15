# vllm-project/vllm#5156: [Feature]: VLLM suport for function calling in Mistral-7B-Instruct-v0.3

| 字段 | 值 |
| --- | --- |
| Issue | [#5156](https://github.com/vllm-project/vllm/issues/5156) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: VLLM suport for function calling in Mistral-7B-Instruct-v0.3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Mistral 7B instruct 0.3 implements function calling, this is a powerfull tool and MistralAi is one of the first to implement it in a "small" model. ```from mistral_common.protocol.instruct.tool_calls import Function, Tool from mistral_inference.model import Transformer from mistral_inference.generate import generate from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from mistral_common.protocol.instruct.messages import UserMessage from mistral_common.protocol.instruct.request import ChatCompletionRequest tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3") model = Transformer.from_folder(mistral_models_path) completion_request = ChatCompletionRequest( tools=[ Tool( function=Function( name="get_current_weather", description="Get the current weather", parameters={ "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA", }, "format": { "type": "string", "enum": ["celsius", "fahrenheit"], "description": "The temperature unit to use. Infer this from the users location.", }, }, "required": ["location", "format"], }, ) ) ], messag...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: full tool and MistralAi is one of the first to implement it in a "small" model. ```from mistral_common.protocol.instruct.tool_calls import Function, Tool from mistral_inference.model import Transformer from mistral_infe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: in a "small" model. ```from mistral_common.protocol.instruct.tool_calls import Function, Tool from mistral_inference.model import Transformer from mistral_inference.generate import generate from mistral_common.tokens.to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: VLLM suport for function calling in Mistral-7B-Instruct-v0.3 feature request ### 🚀 The feature, motivation and pitch Mistral 7B instruct 0.3 implements function calling, this is a powerfull tool and MistralAi is one...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a powerfull tool and MistralAi is one of the first to implement it in a "small" model. ```from mistral_common.protocol.instruct.tool_calls import Function, Tool from mistral_inference.model import Transformer from mistr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
