# vllm-project/vllm#32829: [Bug]: During GLM-4.7 function calling (fc), the function output is not streamed.

| 字段 | 值 |
| --- | --- |
| Issue | [#32829](https://github.com/vllm-project/vllm/issues/32829) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: During GLM-4.7 function calling (fc), the function output is not streamed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the arguments : data: {"id":"chatcmpl-674130d4fca34e2185846e6eef0c6113","object":"chat.completion.chunk","created":1769048523,"model":"GLM-4.7","choices":[{"index":0,"delta":{"content":"","tool_calls":[{"id":"chatcmpl-tool-d70cc2869ec640a1b49c01a0e2d1744d","type":"function","index":0,"function":{"name":"write_to_file","arguments":"{\"filePath\": \"/Users/cyf/Desktop/CODE/\\u5f00\\u6e90\\u9879\\u76ee/cody/style.css\", \"content\": \"* {\\n margin: 0;\\n padding: 0;\\n box-sizing: border-box;\\n}\\n\\nbody {\\n font-family: 'Microsoft YaHei', Arial, sans-serif;\\n background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\\n min-height: 100vh;\\n display: flex;\\n justify-content: center;\\n align-items: center;\\n padding: 20px;\\n}\\n\\n.container {\\n text-align: center;\\n background: white;\\n border-radius: 20px;\\n padding: 30px;\\n box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);\\n}\\n\\nh1 {\\n color: #333;\\n margin-bottom: 20px;\\n font-size: 2.5em;\\n text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);\\n}\\n\\n.game-info {\\n margin-bottom: 20px;\\n}\\n\\n.current-player {\\n font-size: 1.2em;\\n color: #555;\\n margin-bottom...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: display: none;\\n}\\n\\n.cell.black {\\n background: radial-gradient(circle at 30% 30%, #555, #000);\\n border-radius: 50%;\\n box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);\\n z-index: 1;\\n}\\n\\n.cell.white::before,\\n....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: alternate;\\n}\\n\\n@keyframes pulse {\\n from {\\n transform: scale(1);\\n }\\n to {\\n transform: scale(1.1);\\n }\\n}\\n\\n@media (max-width: 600px) {\\n .game-board {\\n grid-template-columns: repeat(15, 25px);\\n g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: }]} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: dius: 50%;\\n z-index: 2;\\n}\\n\\n.cell.winning {\\n animation: pulse 0.5s ease-in-out infinite alternate;\\n}\\n\\n@keyframes pulse {\\n from {\\n transform: scale(1);\\n }\\n to {\\n transform: scale(1.1);\\n }\\n}\\...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 85846e6eef0c6113","object":"chat.completion.chunk","created":1769048523,"model":"GLM-4.7","choices":[{"index":0,"delta":{"content":"","tool_calls":[{"id":"chatcmpl-tool-d70cc2869ec640a1b49c01a0e2d1744d","type":"function...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
