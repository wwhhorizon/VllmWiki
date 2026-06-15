# vllm-project/vllm#23007: [Bug]: GPT OSS 120B token usage is 0 on response API, even though it responded back

| 字段 | 值 |
| --- | --- |
| Issue | [#23007](https://github.com/vllm-project/vllm/issues/23007) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT OSS 120B token usage is 0 on response API, even though it responded back

### Issue 正文摘录

### Your current environment 1xA100, Linux. Launch command: ```bash docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -e VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-oss-120b \ --tensor-parallel-size 1 \ --async-scheduling \ --enable-prompt-tokens-details \ --enable-force-include-usage ``` ### 🐛 Describe the bug ```python # lepton deployment local_url = "http://localhost:8000/v1" client = OpenAI( base_url=local_url, api_key=os.getenv("OPENAI_API_KEY") ) messages = [ {"role": "user", "content": "Hello, I'm learning about geography."}, {"role": "assistant", "content": "Great! I'd be happy to help you learn about geography. What would you like to know?"}, {"role": "user", "content": "What ist the capital of China"} ] response = client.responses.create( model="openai/gpt-oss-120b", instructions="You are a helfpul assistant. Reasoning effort: low", input=messages, ) response ``` Output: ``` Response(id='resp_49afb11438ba421680bc63f615ee2a07', created_at=1755289663.0, error=None, incomplete_details=None, instructions='You are a helfpul assistant. Reasoning effort: low', metadata=None, model='openai/gpt-oss-120b', object='response', out...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: m --gpus all \ -p 8000:8000 \ --ipc=host \ -e VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-oss-120b \ --tensor-parallel-size 1 \ --async-scheduling \ --enable-prompt-tokens-d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Your current environment 1xA100, Linux. Launch command: ```bash docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -e VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: even though it responded back bug;stale ### Your current environment 1xA100, Linux. Launch command: ```bash docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -e VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ vllm/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: None, instructions='You are a helfpul assistant. Reasoning effort: low', metadata=None, model='openai/gpt-oss-120b', object='response', output=[ResponseReasoningItem(id='rs_a2560f61b7734f7cb10802ef4e01a3c0', summary=[],...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-oss-120b \ --tensor-parallel-size 1 \ --async-scheduling \ --enable-prompt-tokens-details \ --enable-force-include-usage ``` ### 🐛 Descri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
