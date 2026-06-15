# vllm-project/vllm#9769: [Bug]: Nonsense output for Qwen2.5 72B after upgrading to latest vllm 0.6.3.post1 [REPROs]

| 字段 | 值 |
| --- | --- |
| Issue | [#9769](https://github.com/vllm-project/vllm/issues/9769) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Nonsense output for Qwen2.5 72B after upgrading to latest vllm 0.6.3.post1 [REPROs]

### Issue 正文摘录

### Your current environment docker 0.6.3.post1 8*A100 ``` docker pull vllm/vllm-openai:latest docker stop qwen25_72b ; docker remove qwen25_72b docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4,5,6,7"' \ --shm-size=10.24gb \ -p 5001:5001 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name qwen25_72b \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=Qwen/Qwen2.5-72B-Instruct \ --tensor-parallel-size=4 \ --seed 1234 \ --trust-remote-code \ --max-model-len=32768 \ --max-num-batched-tokens 131072 \ --max-log-len=100 \ --api-key=EMPTY \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.qwen25_72b.txt ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug No such issues with prior vLLM 0.6.2. Trivial queries work: ``` from openai import OpenAI client = OpenAI(base_url='FILL ME', api_key='FILL ME') messages = [ { "role": "user", "content": "Who are you?", } ] response = client.chat.c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Nonsense output for Qwen2.5 72B after upgrading to latest vllm 0.6.3.post1 [REPROs] bug ### Your current environment docker 0.6.3.post1 8*A100 ``` docker pull vllm/vllm-openai:latest docker stop qwen25_72b ; dock...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng to latest vllm 0.6.3.post1 [REPROs] bug ### Your current environment docker 0.6.3.post1 8*A100 ``` docker pull vllm/vllm-openai:latest docker stop qwen25_72b ; docker remove qwen25_72b docker run -d --restart=always...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .3.post1 [REPROs] bug ### Your current environment docker 0.6.3.post1 8*A100 ``` docker pull vllm/vllm-openai:latest docker stop qwen25_72b ; docker remove qwen25_72b docker run -d --restart=always \ --runtime=nvidia \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Nonsense output for Qwen2.5 72B after upgrading to latest vllm 0.6.3.post1 [REPROs] bug ### Your current environment docker 0.6.3.post1 8*A100 ``` docker pull vllm/vllm-openai:latest docker stop qwen25_72b ; dock...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name qwen25_72b \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=Qwen/Qwen2.5-72B-Instr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
