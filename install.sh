#!/usr/bin/env bash
# ============================================================================
# Sovereign AI Skills — Installer
# Install Claude Code slash commands from the sovereign-ai-skills library.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/MirrorDNA-Reflection-Protocol/sovereign-ai-skills/main/install.sh | bash
#   curl -fsSL ... | bash -s -- --skill forensic
#   curl -fsSL ... | bash -s -- --category sre
#   curl -fsSL ... | bash -s -- --list
#   curl -fsSL ... | bash -s -- --update
#
# --- Built with Active Mirror | activemirror.ai
# ============================================================================

set -euo pipefail

# --- Config ---
REPO_OWNER="MirrorDNA-Reflection-Protocol"
REPO_NAME="sovereign-ai-skills"
BRANCH="main"
BASE_URL="https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}"
SKILLS_URL="${BASE_URL}/skills"
COMMANDS_DIR="${HOME}/.claude/commands"

# --- Colors (safe for pipes — disable if not a terminal) ---
if [ -t 1 ]; then
    BOLD="\033[1m"
    DIM="\033[2m"
    GREEN="\033[32m"
    CYAN="\033[36m"
    YELLOW="\033[33m"
    RED="\033[31m"
    RESET="\033[0m"
else
    BOLD="" DIM="" GREEN="" CYAN="" YELLOW="" RED="" RESET=""
fi

# --- Helpers ---
info()  { printf "${CYAN}>>>${RESET} %s\n" "$*"; }
ok()    { printf "${GREEN} +${RESET} %s\n" "$*"; }
warn()  { printf "${YELLOW} !${RESET} %s\n" "$*"; }
err()   { printf "${RED} x${RESET} %s\n" "$*" >&2; }
die()   { err "$*"; exit 1; }

# --- All skills (canonical list, 144 total) ---
ALL_SKILLS="ab-test adversarial analytics audience audit auto-publish \
backlink backup beacon behind-scenes benchmark brand \
breakthrough brief bus calibrate capability carousel \
cert challenge changelog clip cognitive collab \
commit community-post comparison compete compress content-calendar \
contract cost council cta daily-video decay \
demo dependency deploy device distribution draft \
dream drift drip emergency endscreen engagement \
evergreen evolve experiment factory ffmpeg-reaper find \
focus forensic funnel glossary glyph growth \
guardian handoff hashtag headline health history \
hook idea inbox-zero incident inventory killswitch \
launch link logs meta migrate milestone \
morning-push network newsletter niche-down note og-image \
onboard optimize overnight paper phone-pull pickup \
podcast pr promote prove pulse quote-card \
read reaper recap reflect regression release \
remix replay repurpose research research-agents retire \
review scaffold schedule schema seo-aeo-aio seo-syndication \
series services ship shorts signal sitemap \
smoke snapshot spec stack-video standup status \
storytell swarm sync tag test thread \
thumbnail timelapse trending triage tutorial velocity \
video-essay viral viral-audit weekly-video wire-check youtube-seo"

# --- Category lookup (bash 3.2 compatible — no associative arrays) ---
get_category_skills() {
    local cat="$1"
    case "$cat" in
        sre)
            echo "forensic pulse smoke health status device logs emergency killswitch reaper ffmpeg-reaper wire-check morning-push signal overnight"
            ;;
        devops)
            echo "deploy promote retire services backup migrate release scaffold factory dependency commit pr ship sitemap schema"
            ;;
        security)
            echo "adversarial cert guardian audit regression decay drift"
            ;;
        qa)
            echo "benchmark regression test review smoke snapshot comparison prove"
            ;;
        research)
            echo "experiment prove paper research research-agents dream cognitive council evolve breakthrough"
            ;;
        product)
            echo "capability breakthrough evolve spec milestone launch cost inventory velocity meta challenge"
            ;;
        content)
            echo "draft storytell thread brief newsletter beacon carousel clip community-post headline hook idea note read recap repurpose tutorial behind-scenes quote-card glyph glossary"
            ;;
        analytics)
            echo "analytics growth funnel engagement trending viral viral-audit comparison ab-test niche-down audience distribution optimize"
            ;;
        ops)
            echo "incident replay onboard contract handoff pickup triage inbox-zero standup schedule sync history reflect calibrate compress focus swarm bus"
            ;;
        video)
            echo "daily-video weekly-video video-essay shorts stack-video thumbnail endscreen podcast clip timelapse youtube-seo"
            ;;
        growth)
            echo "seo-aeo-aio seo-syndication backlink hashtag og-image cta brand promote drip content-calendar auto-publish network collab compete evergreen link tag series remix engagement funnel"
            ;;
        *)
            return 1
            ;;
    esac
}

CATEGORY_NAMES="sre devops security qa research product content analytics ops video growth"

# --- Count words in a string ---
word_count() {
    echo "$1" | wc -w | tr -d ' '
}

# --- Check if a skill is in the canonical list ---
skill_exists() {
    local name="$1"
    for s in $ALL_SKILLS; do
        if [ "$s" = "$name" ]; then
            return 0
        fi
    done
    return 1
}

# --- Functions ---

show_banner() {
    printf "\n"
    printf "${BOLD}${CYAN}"
    cat <<'BANNER'
  ____                          _               _    ___   ____  _    _ _ _
 / ___|  _____   _____ _ __ ___(_) __ _ _ __   / \  |_ _| / ___|| | _(_) | |___
 \___ \ / _ \ \ / / _ \ '__/ _ \ |/ _` | '_ \ / _ \  | |  \___ \| |/ / | | / __|
  ___) | (_) \ V /  __/ | |  __/ | (_| | | | / ___ \ | |   ___) |   <| | | \__ \
 |____/ \___/ \_/ \___|_|  \___|_|\__, |_| |_/_/   \_\___| |____/|_|\_\_|_|_|___/
                                  |___/
BANNER
    printf "${RESET}"
    local total
    total=$(word_count "$ALL_SKILLS")
    printf "${DIM}  ${total} Claude Code commands for sovereign AI operations${RESET}\n"
    printf "\n"
}

show_footer() {
    printf "\n${DIM}--- Built with Active Mirror | activemirror.ai${RESET}\n\n"
}

list_categories() {
    printf "${BOLD}Available categories:${RESET}\n\n"
    printf "  ${CYAN}%-12s${RESET} %s\n" "sre"       "System reliability — forensic, pulse, smoke, health, status ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "devops"     "Deployment & infra — deploy, promote, retire, services, ship ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "security"   "Security & hardening — adversarial, cert, guardian, audit ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "qa"         "Quality assurance — benchmark, regression, test, review ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "research"   "Research & science — experiment, prove, paper, research ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "product"    "Product management — capability, spec, milestone, launch ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "content"    "Content creation — draft, storytell, thread, newsletter ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "analytics"  "Data & analytics — analytics, growth, funnel, trending ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "ops"        "Operations — incident, triage, onboard, schedule, sync ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "video"      "Video production — daily-video, shorts, youtube-seo ..."
    printf "  ${CYAN}%-12s${RESET} %s\n" "growth"     "Growth & SEO — seo-aeo-aio, backlink, hashtag, brand ..."
    printf "\n"
}

list_skills() {
    show_banner

    printf "${BOLD}All available skills:${RESET}\n\n"
    local col=0
    for skill in $ALL_SKILLS; do
        printf "  ${CYAN}%-20s${RESET}" "/${skill}"
        col=$((col + 1))
        if [ $((col % 4)) -eq 0 ]; then
            printf "\n"
        fi
    done
    if [ $((col % 4)) -ne 0 ]; then
        printf "\n"
    fi

    printf "\n"
    list_categories
    printf "${DIM}Install one:  install.sh --skill forensic${RESET}\n"
    printf "${DIM}Install cat:  install.sh --category sre${RESET}\n"
    printf "${DIM}Install all:  install.sh${RESET}\n"
    show_footer
}

download_skill() {
    local name="$1"
    local url="${SKILLS_URL}/${name}.md"
    local dest="${COMMANDS_DIR}/${name}.md"

    if curl -fsSL -o "${dest}" "${url}" 2>/dev/null && [ -s "${dest}" ]; then
        return 0
    else
        rm -f "${dest}" 2>/dev/null
        return 1
    fi
}

install_skills() {
    local skills="$1"
    local total
    total=$(word_count "$skills")
    local installed=0
    local failed=0
    local failed_names=""

    mkdir -p "${COMMANDS_DIR}"

    info "Installing ${total} skill(s) to ${COMMANDS_DIR}/"
    printf "\n"

    for skill in $skills; do
        if download_skill "$skill"; then
            ok "/${skill}"
            installed=$((installed + 1))
        else
            warn "/${skill} — download failed"
            failed=$((failed + 1))
            failed_names="${failed_names} ${skill}"
        fi
    done

    printf "\n"
    printf "${BOLD}${GREEN}Installed: ${installed}/${total} skills${RESET}\n"

    if [ "$failed" -gt 0 ]; then
        printf "${YELLOW}Failed: ${failed} —${failed_names}${RESET}\n"
    fi

    printf "${DIM}Location: ${COMMANDS_DIR}/${RESET}\n"
    printf "${DIM}Use in Claude Code: type /skill-name${RESET}\n"
    show_footer
}

# --- Main ---
main() {
    local mode="all"
    local skill_name=""
    local category_name=""

    while [ $# -gt 0 ]; do
        case "$1" in
            --skill|-s)
                mode="skill"
                shift
                [ $# -eq 0 ] && die "--skill requires a skill name. Use --list to see available skills."
                skill_name="$1"
                shift
                ;;
            --category|-c)
                mode="category"
                shift
                [ $# -eq 0 ] && die "--category requires a category name. Use --list to see categories."
                category_name="$1"
                shift
                ;;
            --list|-l)
                mode="list"
                shift
                ;;
            --update|-u)
                mode="update"
                shift
                ;;
            --help|-h)
                mode="help"
                shift
                ;;
            *)
                die "Unknown argument: $1. Use --help for usage."
                ;;
        esac
    done

    case "$mode" in
        help)
            show_banner
            printf "${BOLD}Usage:${RESET}\n\n"
            local total
            total=$(word_count "$ALL_SKILLS")
            printf "  ${CYAN}install.sh${RESET}                      Install all %s skills\n" "$total"
            printf "  ${CYAN}install.sh --skill <name>${RESET}       Install a single skill\n"
            printf "  ${CYAN}install.sh --category <cat>${RESET}     Install all skills in a category\n"
            printf "  ${CYAN}install.sh --list${RESET}               List all available skills & categories\n"
            printf "  ${CYAN}install.sh --update${RESET}             Re-download and update installed skills\n"
            printf "  ${CYAN}install.sh --help${RESET}               Show this help\n"
            printf "\n"
            printf "${BOLD}curl one-liner:${RESET}\n"
            printf "  curl -fsSL https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/install.sh | bash\n"
            printf "  curl -fsSL ... | bash -s -- --skill forensic\n"
            printf "  curl -fsSL ... | bash -s -- --category sre\n"
            show_footer
            ;;
        list)
            list_skills
            ;;
        skill)
            show_banner
            # Strip leading slash if user typed /forensic instead of forensic
            skill_name="${skill_name#/}"
            if ! skill_exists "$skill_name"; then
                die "Unknown skill: ${skill_name}. Use --list to see available skills."
            fi
            install_skills "$skill_name"
            ;;
        category)
            show_banner
            # Lowercase the category name
            category_name=$(printf '%s' "$category_name" | tr '[:upper:]' '[:lower:]')
            local cat_skills
            cat_skills=$(get_category_skills "$category_name") || die "Unknown category: ${category_name}. Use --list to see categories."
            local cat_count
            cat_count=$(word_count "$cat_skills")
            info "Category: ${category_name} (${cat_count} skills)"
            printf "\n"
            install_skills "$cat_skills"
            ;;
        update)
            show_banner
            if [ ! -d "${COMMANDS_DIR}" ]; then
                die "No skills installed yet. Run without --update to install first."
            fi
            local installed_skills=""
            local count=0
            for skill in $ALL_SKILLS; do
                if [ -f "${COMMANDS_DIR}/${skill}.md" ]; then
                    installed_skills="${installed_skills} ${skill}"
                    count=$((count + 1))
                fi
            done
            installed_skills="${installed_skills# }"
            if [ "$count" -eq 0 ]; then
                die "No sovereign-ai-skills found in ${COMMANDS_DIR}/. Run without --update to install."
            fi
            info "Updating ${count} installed skill(s)"
            printf "\n"
            install_skills "$installed_skills"
            ;;
        all)
            show_banner
            install_skills "$ALL_SKILLS"
            ;;
    esac
}

main "$@"
