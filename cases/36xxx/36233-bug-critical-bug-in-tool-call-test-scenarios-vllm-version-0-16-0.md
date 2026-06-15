# vllm-project/vllm#36233: [Bug]:  Critical bug in   tool_call  test scenarios [vllm version 0.16.0]

| 字段 | 值 |
| --- | --- |
| Issue | [#36233](https://github.com/vllm-project/vllm/issues/36233) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Critical bug in   tool_call  test scenarios [vllm version 0.16.0]

### Issue 正文摘录

### Your current environment vLLM version: 0.16.0 and 0.9.2 os:ubuntu2004 model: qwen3_8b **vllm command:** python3 -m vllm.entrypoints.openai.api_server --model /home/szj_project/Qwen3-8B-AWQ-From-TC/ --port 12321 --host 0.0.0.0 --no-enable-prefix-caching --served-model-name qwen3_8b --max-num-seqs 1 --enable-auto-tool-choice --tool-call-parser hermes --max-model-len 32768 --max-num-batched-tokens 32768 vLLM still response tool_call while llamacpp doesn't and the right response should not include tool_call. See following details. ### 🐛 Describe the bug Reproduce and python test code: ``` # 给OpenAI Python库添加日志，打印实际发送的请求体（tool_tester_v2.py中） import logging from openai import OpenAI from tool_definitions import ToolDefinitions all_tools = ToolDefinitions.get_all_tools() # 开启调试日志，打印请求/响应 logging.basicConfig(level=logging.DEBUG) #vllm if 1: client = OpenAI( base_url="http://10.64.33.10:12321/v1", # 确保和curl一致 api_key="sk-123" ) model_name="qwen3_8b" #ollama llamacpp else: client = OpenAI( base_url="http://10.64.33.10:11434/v1", # 确保和curl一致 api_key="sk-123" ) model_name="qwen3:8b" # 执行请求（和curl相同的参数） try: forced_name="get_weather" tool_choice = {"type": "function", "function": {"name": f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Critical bug in tool_call test scenarios [vllm version 0.16.0] bug ### Your current environment vLLM version: 0.16.0 and 0.9.2 os:ubuntu2004 model: qwen3_8b **vllm command:** python3 -m vllm.entrypoints.openai.ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment vLLM version: 0.16.0 and 0.9.2 os:ubuntu2004 model: qwen3_8b **vllm command:** python3 -m vllm.entrypoints.openai.api_server --model /home/szj_project/Qwen3-8B-AWQ-From-TC/ --port 12321 --host 0...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: not include tool_call. See following details. ### 🐛 Describe the bug Reproduce and python test code: ``` # 给OpenAI Python库添加日志，打印实际发送的请求体（tool_tester_v2.py中） import logging from openai import OpenAI from tool_definition...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l_call 请求的 #messages=[{"role":"user","content":"Please use the search_flights tool to find flights from New York to Paris on March 15th, then use get_weather to check the weather in Paris."}], messages= [{'role':'user',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: api_key="sk-123" ) model_name="qwen3_8b" #ollama llamacpp else: client = OpenAI( base_url="http://10.64.33.10:11434/v1", # 确保和curl一致 api_key="sk-123" ) model_name="qwen3:8b" # 执行请求（和curl相同的参数） try: forced_name="get_weat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
