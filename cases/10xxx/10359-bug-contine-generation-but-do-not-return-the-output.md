# vllm-project/vllm#10359: [Bug]: contine generation but do not return the output

| 字段 | 值 |
| --- | --- |
| Issue | [#10359](https://github.com/vllm-project/vllm/issues/10359) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: contine generation but do not return the output

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python class FuncCallOffline: def __init__(self, model_name=None): from vllm import LLM, SamplingParams self.model_name = model_name self.llm = LLM(model=os.environ["MODEL_DIR"], dtype="half") self.sampling_params = SamplingParams(temperature=0.0, max_tokens=1000) token_model = 'gpt-4' self.encoding = tiktoken.encoding_for_model(token_model) def llm_func(self, messages, model_name): #pdb.set_trace() outputs = self.llm.chat(messages, sampling_params=self.sampling_params) text = outputs[0].outputs[0].text.strip() return text ``` There is no problem with the generation at the beginning, but suddenly there is no output, no error is reported, and it will remain in this state ```error Processed prompts: 100%|█| 1/1 [00:03<00:00, 3.76s/it, est. speed input: 269.20 toks/s Processed prompts: 100%|█| 1/1 [00:03<00:00, 3.76s/it, est. speed input: 269.43 toks/s Processed prompts: 100%|█| 1/1 [00:03<00:00, 3.78s/it, est. speed input: 267.67 toks/s Processed prompts: 100%|█| 1/1 [00:03<00:00, 3.77s/it, est. speed input: 268.94 toks/s Processed prompts: 100%|█| 1/1 [00:03<00:00, 3.77s/it, est. speed input:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CallOffline: def __init__(self, model_name=None): from vllm import LLM, SamplingParams self.model_name = model_name self.llm = LLM(model=os.environ["MODEL_DIR"], dtype="half") self.sampling_params = SamplingParams(tempe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _name = model_name self.llm = LLM(model=os.environ["MODEL_DIR"], dtype="half") self.sampling_params = SamplingParams(temperature=0.0, max_tokens=1000) token_model = 'gpt-4' self.encoding = tiktoken.encoding_for_model(to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on but do not return the output bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python class FuncCallOffline: def __init__(self, model_name=None): from vllm import LLM, Sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
